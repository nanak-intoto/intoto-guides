(function(){
  if (window.__intotoFeatureFlowAnimations) return;
  window.__intotoFeatureFlowAnimations = true;

  var reducedMotion = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : { matches:false };
  var timerMap = new WeakMap();
  var roleMeta = {
    student:{ actor:'Student / user', badge:'User action', note:'A user-facing action in the product experience.' },
    admin:{ actor:'Coordinator / admin', badge:'Admin action', note:'Operational staff review, publish, moderate, or approve.' },
    university:{ actor:'University admin', badge:'Governance', note:'Tenant-level control, reporting, and entitlement visibility.' },
    decision:{ actor:'Decision point', badge:'Decision', note:'The workflow branches based on approval, rejection, or missing information.' },
    flow:{ actor:'System handoff', badge:'Information moves', note:'The output from one step becomes the input for the next step.' },
    step:{ actor:'Workflow step', badge:'Process', note:'Part of the end-to-end feature workflow.' }
  };

  function itemsFor(diagram){
    return Array.prototype.slice.call(diagram.querySelectorAll('.flow-node-card, .flow-arrow'));
  }

  function roleFor(item){
    if (item.classList.contains('flow-arrow')) return 'flow';
    if (item.classList.contains('student')) return 'student';
    if (item.classList.contains('admin')) return 'admin';
    if (item.classList.contains('university')) return 'university';
    if (item.classList.contains('success') || item.classList.contains('warning') || item.classList.contains('danger')) return 'decision';
    return 'step';
  }

  function text(item, selector, fallback){
    var found = item ? item.querySelector(selector) : null;
    return found && found.textContent ? found.textContent.trim() : fallback;
  }

  function nearbyCard(items, index, direction){
    for (var i = index + direction; i >= 0 && i < items.length; i += direction) {
      if (items[i].classList.contains('flow-node-card')) return items[i];
    }
    return null;
  }

  function detailsFor(item, role){
    if (role === 'flow') {
      return {
        info:'Relevant record, status, documents, notes, and IDs are passed forward.',
        review:'The next screen opens with the previous step already in context.',
        result:'The next actor continues without asking the user to re-enter the same information.'
      };
    }
    return {
      info:item.getAttribute('data-info') || 'The screen captures the details needed for this step.',
      review:item.getAttribute('data-review') || 'The responsible role checks completeness, eligibility, policy, and status.',
      result:item.getAttribute('data-result') || 'The workflow updates and the next action becomes visible.'
    };
  }

  function storyFor(diagram, item, index, total){
    var role = roleFor(item);
    var meta = roleMeta[role] || roleMeta.step;
    var details = detailsFor(item, role);
    if (role === 'flow') {
      var items = itemsFor(diagram);
      var previous = nearbyCard(items, index, -1);
      var next = nearbyCard(items, index, 1);
      return {
        actor:meta.actor,
        badge:meta.badge,
        note:meta.note,
        title:'Handoff: ' + text(previous, '.title', 'previous step') + ' to ' + text(next, '.title', 'next step'),
        copy:'The product carries the latest state forward so the next user or screen knows exactly what happened.',
        outcome:'Outcome: the next person sees the right record with the right status.',
        details:details
      };
    }
    return {
      actor:item.getAttribute('data-actor') || meta.actor,
      badge:meta.badge,
      note:meta.note,
      title:text(item, '.title', 'Workflow step'),
      copy:text(item, 'p', 'This step advances the feature workflow.'),
      outcome:'Outcome: ' + details.result,
      details:details,
      step:index + 1,
      total:total
    };
  }

  function ensurePanel(diagram){
    var controls = diagram.querySelector('.flow-controls');
    if (!controls) {
      controls = document.createElement('div');
      controls.className = 'flow-controls';
      controls.innerHTML = '<button class="flow-play" type="button">Play Story</button><div class="flow-progress"><div class="flow-progress-bar"></div></div><div class="flow-legend"><span class="student">User</span><span class="admin">Admin</span><span class="university">University</span><span class="decision">Decision</span></div>';
      diagram.insertBefore(controls, diagram.firstChild.nextSibling);
    }

    var panel = diagram.querySelector('.flow-story-panel');
    if (!panel) {
      panel = document.createElement('div');
      panel.className = 'flow-story-panel';
      panel.innerHTML = '<div class="flow-story-actor"><span class="eyebrow">Current actor</span><strong>Ready</strong><small>Press Play Story to see who does what.</small></div><div class="flow-story-body"><div class="flow-story-kicker">Step by step</div><div class="flow-story-title">Feature flow animation</div><p class="flow-story-copy">The animation explains data collection, review, and approval outcomes.</p><p class="flow-story-outcome">Outcome: waiting to begin.</p><div class="flow-story-details"><div class="flow-detail-card"><b>Information taken</b><span>Step-specific data will appear here.</span></div><div class="flow-detail-card"><b>How it is reviewed</b><span>Review logic will appear here.</span></div><div class="flow-detail-card"><b>Decision / result</b><span>Result will appear here.</span></div></div></div>';
      diagram.insertBefore(panel, controls.nextSibling);
    }
  }

  function updateStory(diagram, item, index, total){
    var story = storyFor(diagram, item, index, total);
    var panel = diagram.querySelector('.flow-story-panel');
    if (!panel) return;
    panel.querySelector('.flow-story-actor strong').textContent = story.actor;
    panel.querySelector('.flow-story-actor small').textContent = story.note;
    panel.querySelector('.flow-story-kicker').textContent = story.badge + (story.step ? ' · ' + story.step + ' of ' + story.total : '');
    panel.querySelector('.flow-story-title').textContent = story.title;
    panel.querySelector('.flow-story-copy').textContent = story.copy;
    panel.querySelector('.flow-story-outcome').textContent = story.outcome;
    var detailCards = panel.querySelectorAll('.flow-detail-card span');
    if (detailCards[0]) detailCards[0].textContent = story.details.info;
    if (detailCards[1]) detailCards[1].textContent = story.details.review;
    if (detailCards[2]) detailCards[2].textContent = story.details.result;
  }

  function clearTimers(diagram){
    var timers = timerMap.get(diagram) || [];
    timers.forEach(function(timer){ clearTimeout(timer); });
    timerMap.set(diagram, []);
  }

  function prepare(diagram){
    if (diagram.dataset.flowReady) return;
    ensurePanel(diagram);
    var items = itemsFor(diagram);
    items.forEach(function(item){
      var role = roleFor(item);
      if (role !== 'flow') item.setAttribute('data-flow-role-label', roleMeta[role].badge);
    });
    diagram.dataset.flowReady = 'true';
    updateStory(diagram, items[0], 0, items.length);
    var playButton = diagram.querySelector('.flow-play');
    if (playButton) {
      playButton.addEventListener('click', function(){ play(diagram, true); });
    }
  }

  function finish(diagram){
    var items = itemsFor(diagram);
    items.forEach(function(item){ item.classList.remove('flow-active'); item.classList.add('flow-seen'); });
    var progress = diagram.querySelector('.flow-progress-bar');
    if (progress) progress.style.width = '100%';
    var playButton = diagram.querySelector('.flow-play');
    if (playButton) {
      playButton.textContent = 'Replay Story';
      playButton.disabled = false;
      playButton.style.opacity = '';
    }
    diagram.classList.add('flow-complete');
  }

  function play(diagram, manual){
    prepare(diagram);
    if (reducedMotion.matches && !manual) {
      finish(diagram);
      return;
    }
    clearTimers(diagram);
    var items = itemsFor(diagram);
    var progress = diagram.querySelector('.flow-progress-bar');
    var playButton = diagram.querySelector('.flow-play');
    diagram.classList.remove('flow-complete');
    items.forEach(function(item){ item.classList.remove('flow-seen', 'flow-active'); });
    if (progress) progress.style.width = '0%';
    if (playButton) {
      playButton.textContent = 'Playing...';
      playButton.disabled = true;
      playButton.style.opacity = '.72';
    }
    var timers = [];
    items.forEach(function(item, index){
      timers.push(setTimeout(function(){
        items.forEach(function(other){ other.classList.remove('flow-active'); });
        item.classList.add('flow-seen', 'flow-active');
        updateStory(diagram, item, index, items.length);
        if (progress) progress.style.width = Math.round(((index + 1) / items.length) * 100) + '%';
      }, index * 880));
    });
    timers.push(setTimeout(function(){ finish(diagram); }, items.length * 880 + 320));
    timerMap.set(diagram, timers);
  }

  function init(){
    var diagrams = Array.prototype.slice.call(document.querySelectorAll('.flow-visual[data-flow-animated]'));
    diagrams.forEach(prepare);
    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function(entries){
        entries.forEach(function(entry){
          if (entry.isIntersecting && !entry.target.dataset.flowPlayed) {
            entry.target.dataset.flowPlayed = 'true';
            play(entry.target, false);
          }
        });
      }, { threshold:.45 });
      diagrams.forEach(function(diagram){ observer.observe(diagram); });
    } else {
      diagrams.forEach(function(diagram){ play(diagram, false); });
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
