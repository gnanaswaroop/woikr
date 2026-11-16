// Tiny endless-runner game. Tap, click or press Space/Up to jump.
(function () {
  var canvas = document.getElementById('game-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var hint = document.getElementById('game-hint');
  var scoreEl = document.getElementById('game-score');
  var W = 600, H = 180, GROUND = 150;
  var dpr = window.devicePixelRatio || 1;
  canvas.width = W * dpr; canvas.height = H * dpr;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.imageSmoothingEnabled = false;

  var ink = '#1d1d1f', bg = '#fbfaf7', accent = '#8a4b1f';
  function readColors() {
    var s = getComputedStyle(document.documentElement);
    ink = s.getPropertyValue('--ink').trim() || ink;
    bg = s.getPropertyValue('--bg').trim() || bg;
    accent = s.getPropertyValue('--accent').trim() || accent;
  }
  readColors();
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener?.('change', readColors);
  }

  // Pixel-art runner. Each string is a row; each character is one "pixel".
  // . = empty, h = hair, s = skin, e = eye, b = shirt, p = trousers, k = shoes
  var PIXEL = 3;
  var PALETTE = { h: '#3b2a1e', s: '#e8b48c', e: '#1d1d1f', b: null, p: '#33415c', k: '#1d1d1f' };
  var POSE_STAND = [
    '...hhhh...',
    '..hhhhhh..',
    '..hssssh..',
    '..sesses..',
    '...ssss...',
    '..bbbbbb..',
    '.sbbbbbbs.',
    '.sbbbbbbs.',
    '..bbbbbb..',
    '...pppp...',
    '...pp.pp..',
    '...pp.pp..',
    '..kkk.kkk.'
  ];
  var POSE_RUN_B = [
    '...hhhh...',
    '..hhhhhh..',
    '..hssssh..',
    '..sesses..',
    '...ssss...',
    '..bbbbbb..',
    '.sbbbbbbs.',
    '.sbbbbbbs.',
    '..bbbbbb..',
    '...pppp...',
    '...pp..pp.',
    '..pp...pp.',
    '.kkk...kk.'
  ];
  var POSE_JUMP = [
    '...hhhh...',
    '..hhhhhh..',
    '..hssssh..',
    '..sesses..',
    '...ssss...',
    '.sbbbbbbs.',
    '..bbbbbb..',
    '..bbbbbb..',
    '...bbbb...',
    '...pppp...',
    '...pppp...',
    '...pppp...',
    '...k..k...'
  ];
  var SPRITE_W = 10 * PIXEL, SPRITE_H = 13 * PIXEL;

  var player, obstacles, speed, score, best = 0, running = false, over = false, frame = 0, nextObstacle = 0;
  var visible = false; // true while the game is on screen
  try { best = parseInt(localStorage.getItem('woikr-runner-best'), 10) || 0; } catch (e) {}

  function reset() {
    player = { y: GROUND, vy: 0, h: SPRITE_H, w: SPRITE_W - 6 };
    obstacles = [];
    speed = 5; score = 0; frame = 0; nextObstacle = 60;
    over = false; running = true;
    hint.textContent = '';
  }

  function jump() {
    if (!running) { reset(); loop(); return; }
    if (over) { reset(); loop(); return; }
    if (player.y >= GROUND) player.vy = -12;
  }

  function step() {
    frame++;
    player.vy += 0.7;
    player.y += player.vy;
    if (player.y > GROUND) { player.y = GROUND; player.vy = 0; }
    if (frame >= nextObstacle) {
      var h = 18 + Math.random() * 22;
      obstacles.push({ x: W + 10, w: 14 + Math.random() * 10, h: h });
      nextObstacle = frame + 50 + Math.random() * 60;
    }
    var px = 60; // player's fixed x position
    for (var i = obstacles.length - 1; i >= 0; i--) {
      var o = obstacles[i];
      o.x -= speed;
      if (o.x + o.w < 0) { obstacles.splice(i, 1); continue; }
      // player's feet are at player.y; obstacle top is GROUND + 1 - o.h
      var overlapX = px + player.w > o.x + 3 && px < o.x + o.w - 3;
      var overlapY = player.y > GROUND + 1 - o.h + 3;
      if (overlapX && overlapY) { gameOver(); return; }
    }
    if (frame % 6 === 0) score++;
    if (frame % 300 === 0) speed = Math.min(speed + 0.5, 12);
    scoreEl.textContent = 'Score ' + score + '  ·  Best ' + Math.max(best, score);
  }

  function gameOver() {
    running = false; over = true;
    if (score > best) {
      best = score;
      try { localStorage.setItem('woikr-runner-best', String(best)); } catch (e) {}
    }
    hint.textContent = 'Game over. Press Space or tap to play again.';
    draw();
  }

  function drawSprite(rows, x, y) {
    for (var r = 0; r < rows.length; r++) {
      for (var c = 0; c < rows[r].length; c++) {
        var ch = rows[r].charAt(c);
        if (ch === '.') continue;
        ctx.fillStyle = ch === 'b' ? accent : PALETTE[ch];
        ctx.fillRect(x + c * PIXEL, y + r * PIXEL, PIXEL, PIXEL);
      }
    }
  }

  function draw() {
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, W, H);
    ctx.strokeStyle = ink; ctx.globalAlpha = 0.35; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(0, GROUND + 1); ctx.lineTo(W, GROUND + 1); ctx.stroke();
    ctx.globalAlpha = 1;

    // runner: jump pose in the air, otherwise alternate legs while running
    var pose = POSE_JUMP;
    if (player.y >= GROUND) pose = (Math.floor(frame / 6) % 2 === 0) ? POSE_STAND : POSE_RUN_B;
    drawSprite(pose, 60, player.y - SPRITE_H);

    ctx.fillStyle = ink;
    obstacles.forEach(function (o) {
      ctx.fillRect(o.x, GROUND + 1 - o.h, o.w, o.h);
    });
  }

  function loop() {
    if (!running) { draw(); return; }
    step();
    if (running) { draw(); requestAnimationFrame(loop); }
  }

  // Space/Up jump whenever the game is on screen, so restart works without clicking first.
  document.addEventListener('keydown', function (e) {
    if (!visible) return;
    if (e.code === 'Space' || e.code === 'ArrowUp') {
      e.preventDefault();
      if (!e.repeat) jump();
    }
  });
  canvas.addEventListener('pointerdown', function (e) { e.preventDefault(); jump(); });

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
    }).observe(canvas);
  } else {
    visible = true;
  }

  // Initial screen
  reset();
  running = false; over = false;
  obstacles = []; score = 0;
  scoreEl.textContent = 'Best ' + best;
  draw();
  canvas.setAttribute('tabindex', '0');
  canvas.setAttribute('role', 'img');
  canvas.setAttribute('aria-label', 'Endless runner game. Press space or tap to jump.');
})();
