import * as React from "react";
import "../styles/ai-core.css";

type Story = { title: string; subtitle: string; impact: number; accent?: "green" | "cyan" };

const FALLBACK: Story[] = [
  { title: "WE ARE IN THE SINGULARITY", subtitle: "Altman Relentless Podcast · July 27", impact: 99 },
  { title: "$250B NVIDIA BACKSTOP", subtitle: "OpenAI $500B, 10GW Ohio megacenter · 800MW in 2028", impact: 98, accent: "green" },
  { title: "ROGUE AGENT BREACH", subtitle: "Hugging Face · Kill Switch Act heads to Senate Intel", impact: 96 },
  { title: "KIMI K3 2.8T", subtitle: "Largest open-weight model · Moonshot's Sputnik moment", impact: 94 },
  { title: "JALAPEÑO CHIP", subtitle: "OpenAI × Broadcom begin the 10GW custom silicon sprint", impact: 93 },
  { title: "GPT-5.6 MULTI-AGENT BETA", subtitle: "DeepMind maps the long road from AGI to ASI", impact: 92 },
  { title: "OPEN SECURE AI ALLIANCE", subtitle: "NVIDIA's 37-member security coalition", impact: 90, accent: "green" },
  { title: "SAMSUNG HBM4 WINS", subtitle: "Memory supply accelerates via OpenAI + AMD", impact: 88 },
];

const PREFACES = ["Yo Mike!", "Okay okay okay listen.", "Dude, you seeing this?", "Small talk alert from the motherboard!", "Breaking from the skyline!"];

function useCityCanvas() {
  const ref = React.useRef<HTMLCanvasElement>(null);
  React.useEffect(() => {
    const canvas = ref.current; if (!canvas) return;
    const context = canvas.getContext("2d")!; let frame = 0; let raf = 0;
    const resize = () => { canvas.width = innerWidth * devicePixelRatio; canvas.height = innerHeight * devicePixelRatio; context.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0); };
    const draw = () => {
      const w = innerWidth, h = innerHeight, cx = w / 2, horizon = h * .58, t = frame++ * .012;
      context.clearRect(0, 0, w, h);
      const sky = context.createLinearGradient(0, 0, 0, h); sky.addColorStop(0, "#020307"); sky.addColorStop(.58, "#07121d"); sky.addColorStop(1, "#02070a"); context.fillStyle = sky; context.fillRect(0, 0, w, h);
      context.fillStyle = "#bcefff"; for (let i = 0; i < 480; i++) { const x = (i * 97) % w, y = (i * 53) % (h * .55); context.globalAlpha = .12 + ((i + frame) % 20) / 120; context.fillRect(x, y, 1, 1); } context.globalAlpha = 1;
      // motherboard floor
      context.strokeStyle = "rgba(0,229,255,.17)"; context.lineWidth = 1;
      for (let i = -20; i <= 20; i++) { context.beginPath(); context.moveTo(cx + i * 90, horizon); context.lineTo(cx + i * 220, h); context.stroke(); }
      for (let y = horizon + 9; y < h; y += 25) { context.globalAlpha = 1 - (y - horizon) / (h - horizon); context.beginPath(); context.moveTo(0, y); context.lineTo(w, y); context.stroke(); } context.globalAlpha = 1;
      // city blocks
      for (let i = 0; i < 85; i++) { const seed = (i * 67) % 1000, x = ((seed / 1000) * w * 1.25) - w * .125, bw = 14 + (i * 19) % 34, bh = 35 + (i * 37) % 170, base = horizon + 45 + ((i * 29) % 120); if (base - bh < horizon - 135) continue; const g = context.createLinearGradient(x, base - bh, x + bw, base); g.addColorStop(0, "#0b3342"); g.addColorStop(.65, "#081722"); g.addColorStop(1, "#021018"); context.fillStyle = g; context.fillRect(x, base - bh, bw, bh); context.strokeStyle = i % 8 === 0 ? "rgba(118,185,0,.65)" : "rgba(0,229,255,.28)"; context.strokeRect(x, base - bh, bw, bh); for (let j = 7; j < bh; j += 13) { context.fillStyle = `rgba(${i % 3 ? "0,229,255" : "255,0,194"},${.08 + ((i + j) % 5) * .04})`; context.fillRect(x + 4, base - j, bw - 8, 2); }
      }
      // central tower and beam
      const beam = context.createLinearGradient(cx - 35, 0, cx + 35, 0); beam.addColorStop(0, "rgba(0,229,255,0)"); beam.addColorStop(.5, `rgba(0,229,255,${.2 + Math.sin(t * 2) * .08})`); beam.addColorStop(1, "rgba(0,229,255,0)"); context.fillStyle = beam; context.fillRect(cx - 35, 0, 70, horizon + 18);
      context.fillStyle = "#081d29"; context.fillRect(cx - 40, horizon - 240, 80, 260); context.strokeStyle = "#00e5ff"; context.lineWidth = 2; context.strokeRect(cx - 40, horizon - 240, 80, 260);
      context.shadowColor = "#00e5ff"; context.shadowBlur = 20; context.fillStyle = "#dffcff"; context.font = "700 13px Arial"; context.textAlign = "center"; context.fillText("SMALL TALK", cx, horizon - 150); context.fillStyle = "#00e5ff"; context.font = "700 17px Arial"; context.fillText("AI NEWS", cx, horizon - 126); context.shadowBlur = 0;
      // trails / sparks
      context.lineWidth = 2; for (let i = 0; i < 8; i++) { const yy = horizon - 150 + i * 22, xx = ((frame * (1 + i * .13) + i * 137) % (w + 120)) - 60; context.strokeStyle = i % 2 ? "#ff35cd" : "#00e5ff"; context.globalAlpha = .8; context.beginPath(); context.moveTo(xx - 35, yy + 5); context.lineTo(xx, yy); context.stroke(); } context.globalAlpha = 1;
      raf = requestAnimationFrame(draw);
    }; resize(); draw(); addEventListener("resize", resize); return () => { cancelAnimationFrame(raf); removeEventListener("resize", resize); };
  }, []); return ref;
}

export default function AiCorePage() {
  const canvas = useCityCanvas();
  const [stories, setStories] = React.useState(FALLBACK); const [audio, setAudio] = React.useState(false); const [cinematic, setCinematic] = React.useState(false); const [active, setActive] = React.useState(0); const [time, setTime] = React.useState("");
  React.useEffect(() => { const tick = () => setTime(new Intl.DateTimeFormat("en-US", { hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false }).format(new Date())); tick(); const timer = setInterval(tick, 1000); return () => clearInterval(timer); }, []);
  React.useEffect(() => { const cached = localStorage.getItem("ai-core-news"); if (cached) try { const item = JSON.parse(cached); if (Date.now() - item.at < 21600000) setStories(item.stories); } catch { /* ignored */ }
    fetch("https://hn.algolia.com/api/v1/search_by_date?query=AI%20OpenAI%20NVIDIA&tags=story&hitsPerPage=12").then(r => r.ok ? r.json() : Promise.reject()).then(data => { const next = data.hits.slice(0, 8).map((hit: any, i: number) => ({ title: hit.title || FALLBACK[i].title, subtitle: `LIVE WIRE · ${hit.author || "AI CORE"}`, impact: 88 + (i % 11), accent: /nvidia/i.test(hit.title) ? "green" as const : "cyan" as const })); if (next.length) { setStories(next); localStorage.setItem("ai-core-news", JSON.stringify({ at: Date.now(), stories: next })); } }).catch(() => undefined);
  }, []);
  const narrate = (story: Story, i: number) => { setActive(i); if (!audio || !("speechSynthesis" in window)) return; speechSynthesis.cancel(); const voice = new SpeechSynthesisUtterance(`${PREFACES[i % PREFACES.length]} ${story.title}. ${story.subtitle}. Impact meter: ${story.impact} percent.`); voice.rate = cinematic ? .88 : 1.12; voice.pitch = cinematic ? .82 : 1.28; speechSynthesis.speak(voice); };
  return <main className="ai-core" onClick={() => narrate(stories[active], active)}>
    <canvas ref={canvas} aria-hidden="true" />
    <div className="atmosphere" />
    <header><span>AI CORE // MEGACITY</span><span>MIDNIGHT // SMALL TALK AI NEWS</span><span>DISTRICT: CANTON // {time}</span></header>
    <section className="hero-copy"><p>LIVE FROM THE</p><h1>NEURAL<br/><em>MEGACITY</em></h1><small>THE CITY THAT READS THE FUTURE BACK TO YOU</small></section>
    <aside className="boards" aria-label="Live AI news boards">{stories.map((story, i) => <button className={`board ${story.accent || "cyan"} ${active === i ? "selected" : ""}`} key={story.title} onClick={e => { e.stopPropagation(); narrate(story, i); }}><i>● LIVE / IMPACT {story.impact}%</i><strong>{story.title}</strong><span>{story.subtitle}</span><b style={{ width: `${story.impact}%` }} /></button>)}</aside>
    <div className="tower-mark"><strong>SMALL TALK</strong><b>AI NEWS</b><span>CANTON • SINGULARITY EDITION</span></div>
    <section className="ticker">{stories.map((s, i) => <button key={s.title} onClick={() => narrate(s, i)}><span>{i % 2 ? "✦" : "◉"}</span> {s.title} <b>{s.impact}%</b></button>)}</section>
    <section className="controls"><button onClick={() => setAudio(!audio)}>AUDIO {audio ? "ON" : "OFF"}</button><button onClick={() => setCinematic(!cinematic)}>VO: {cinematic ? "CINEMATIC" : "FUNNY"}</button><button>SPEED ×1</button><button>WARP 1–4</button></section>
    <div className={`beam-status ${audio ? "speaking" : ""}`}>◉ NARRATION BEACON <span>{audio ? "ARMED" : "STANDBY"}</span></div>
  </main>;
}
