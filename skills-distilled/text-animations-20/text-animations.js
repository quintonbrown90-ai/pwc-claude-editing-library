// 20 Text Animations — JS engine. TextFX.run(slug, element, opts)
// opts: {text, target (count-up), suffix, label, duration, accent}
const GLYPHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#%&$?!';
const rnd = s => s[Math.floor(Math.random()*s.length)];
function splitChars(el, text){ el.innerHTML=''; [...text].forEach((c,i)=>{ const s=document.createElement('span');
  s.className='fx-ch'; s.style.setProperty('--i', i); s.textContent = c===' ' ? '\u00A0' : c; el.appendChild(s); }); return el.children; }
function extrude(el, depthPx, color){ const n=Math.max(2, Math.round(depthPx)); const parts=[];
  for(let i=1;i<=n;i++) parts.push(`${(i/n*depthPx).toFixed(1)}px ${(i/n*depthPx).toFixed(1)}px 0 ${color}`);
  el.style.textShadow = parts.join(','); }

const TextFX = {
  run(slug, el, opts={}){ el.classList.add('fx'); const text = opts.text ?? el.dataset.text ?? el.textContent.trim();
    const D = opts.duration; if(this[slug]) this[slug](el, text, opts, D); else el.classList.add('fx-'+slug); },

  'typewriter'(el, text, o){ el.innerHTML=''; const out=document.createElement('span'); const caret=document.createElement('span');
    caret.className='fx-caret'; el.append(out, caret); let i=0; const step = o.stepMs ?? 55;
    const t=setInterval(()=>{ out.textContent=text.slice(0,++i); if(i>=text.length){ clearInterval(t);
      setTimeout(()=>caret.remove(), 900); } }, step); },

  'word-stagger'(el, text, o){ const words=text.split(' '); el.innerHTML=''; words.forEach((w,i)=>{ const s=document.createElement('span');
      s.className='fx-ch'; s.textContent=w; s.style.opacity=0; s.style.transform='translateY(.12em)';
      s.style.transition=`all .3s ease-out ${i*.18}s`; el.append(s, document.createTextNode(' '));
      requestAnimationFrame(()=>{ s.style.opacity=1; s.style.transform='none'; });
      if(i===words.length-1){ s.style.background='#111'; s.style.color='var(--fx-accent)';
        s.style.padding='0 .18em'; s.style.borderRadius='.08em'; } }); },

  'number-count-up'(el, text, o){ const target = o.target ?? parseFloat(text.replace(/[^0-9.]/g,'')) ?? 10000;
    const dur = o.duration ?? 1200; const t0 = performance.now();
    const fmt = n => Math.round(n).toLocaleString('en-US');
    const tick = now => { const p = Math.min(1, (now-t0)/dur); const e = 1-Math.pow(1-p, 4);
      el.textContent = fmt(target*e) + (p>=0.98 ? (o.suffix ?? '') : '');
      if(p<1) requestAnimationFrame(tick); }; requestAnimationFrame(tick); },

  'scramble-decode'(el, text, o){ this._scramble(el, text, o, true); },
  'decode-marker'(el, text, o){ el.style.position='relative';
    this._scramble(el, text, o, false, ()=>{ const band=document.createElement('span');
      band.style.cssText='position:absolute;inset:0 -.1em;background:#111;z-index:-1;transform:scaleX(0);transform-origin:left;transition:transform .35s cubic-bezier(.6,.02,.3,1)';
      el.appendChild(band); el.style.color='var(--fx-accent)'; requestAnimationFrame(()=>band.style.transform='scaleX(1)'); }); },
  _scramble(el, text, o, accentLock, done){ const dur = o.duration ?? (accentLock?900:700); const t0=performance.now();
    const iv=setInterval(()=>{ const p=(performance.now()-t0)/dur; const locked=Math.floor(p*text.length);
      el.childNodes.forEach(n=>{ if(n.nodeType===1 && n.tagName==='SPAN' && n.style.position==='absolute') n.remove(); });
      el.textContent=''; [...text].forEach((c,i)=>{ const s=document.createElement('span');
        if(i<locked){ s.textContent=c; if(accentLock) s.style.color='var(--fx-accent)'; }
        else s.textContent = c===' ' ? ' ' : rnd(GLYPHS); el.appendChild(s); });
      if(p>=1){ clearInterval(iv); el.textContent=text; if(accentLock) el.style.color='var(--fx-accent)'; done && done(); } }, 45); },

  'sine-wave'(el, text, o){ const chars=splitChars(el, text); const amp=o.amplitude ?? .18;
    const loop=t=>{ [...chars].forEach((s,i)=>{ const v=Math.sin(t/190 + i*.55);
      s.style.transform=`translateY(${(-v*amp).toFixed(3)}em)`;
      s.style.color = v>0.55 ? 'var(--fx-accent)' : ''; }); requestAnimationFrame(loop); };
    requestAnimationFrame(loop); },

  '3d-extrude'(el, text, o){ el.style.color='var(--fx-accent)'; const max=o.depth ?? 10; const t0=performance.now();
    const tick=now=>{ const p=Math.min(1,(now-t0)/600); extrude(el, max*(1-Math.pow(1-p,3)), 'var(--fx-accent-dark)');
      if(p<1) requestAnimationFrame(tick); }; requestAnimationFrame(tick); },

  'outline-extrude'(el, text, o){ el.classList.add('fx-outline-extrude'); const t0=performance.now();
    const tick=now=>{ const p=Math.min(1,(now-t0)/900);
      if(p<.39){ el.style.opacity = .35 + .65*(p/.39); }
      else { const q=(p-.39)/.61; el.style.color=`color-mix(in srgb, var(--fx-accent) ${Math.round(q*100)}%, transparent)`;
        extrude(el, 7*(1-Math.pow(1-q,3)), 'var(--fx-accent-dark)'); }
      if(p<1) requestAnimationFrame(tick); }; requestAnimationFrame(tick); },

  'liquid-fill'(el, text, o){ const chars=splitChars(el, text);
    [...chars].forEach((s,i)=>{ s.style.color='transparent'; s.style.webkitTextStroke='.02em currentColor';
      s.style.background='linear-gradient(to top, var(--fx-accent) 50%, transparent 50%)';
      s.style.backgroundSize='100% 220%'; s.style.backgroundPosition='0 0'; s.style.webkitBackgroundClip='text';
      s.style.transition=`background-position .25s ease-in-out ${i*.08}s`;
      requestAnimationFrame(()=>{ s.style.backgroundPosition='0 100%'; s.style.webkitTextStroke='.02em var(--fx-accent)'; }); }); },

  'letter-flip'(el, text){ splitChars(el, text); el.classList.add('fx-letter-flip'); },
  'blur-bounce'(el, text){ splitChars(el, text); el.classList.add('fx-blur-bounce'); },
  'split-reveal'(el, text, o){ const top=text, pill=o.pill ?? 'REVEAL';
    el.innerHTML=`<span class="fx-half" style="height:.52em"><span class="fx-top">${top}</span></span>`+
      `<span class="fx-half" style="height:.52em"><span class="fx-bot" style="transform:translateY(-.48em)">${top}</span></span>`+
      `<span class="fx-pill">${pill}</span>`; el.classList.add('fx-split-reveal');
    requestAnimationFrame(()=>requestAnimationFrame(()=>el.classList.add('go'))); },

  'rise-squiggle'(el, text, o){ const chars=splitChars(el, text);
    [...chars].forEach((s,i)=>{ s.style.transform='translateY(.6em)'; s.style.opacity=0;
      s.style.transition=`all .4s cubic-bezier(.22,.8,.32,1) ${i*.03}s`;
      requestAnimationFrame(()=>{ s.style.transform='none'; s.style.opacity=1; }); });
    const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
    svg.setAttribute('viewBox','0 0 200 12'); svg.style.cssText='position:absolute;left:0;right:0;bottom:-.35em;width:100%;height:.18em';
    const path=document.createElementNS('http://www.w3.org/2000/svg','path');
    path.setAttribute('d','M2 8 Q 12 2, 25 8 T 50 8 T 75 8 T 100 8 T 125 8 T 150 8 T 175 8 T 198 8');
    path.setAttribute('fill','none'); path.setAttribute('stroke','var(--fx-accent)'); path.setAttribute('stroke-width','3');
    const len=220; path.style.strokeDasharray=len; path.style.strokeDashoffset=len;
    path.style.transition='stroke-dashoffset .5s ease-in-out .35s'; svg.appendChild(path); el.appendChild(svg);
    requestAnimationFrame(()=>path.style.strokeDashoffset=0); },
};
window.TextFX = TextFX;
document.querySelectorAll('[data-fx]').forEach(el=>TextFX.run(el.dataset.fx, el, { target: el.dataset.target ? +el.dataset.target : undefined, suffix: el.dataset.suffix }));
