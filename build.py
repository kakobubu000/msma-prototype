#!/usr/bin/env python3
"""
Builds index.html for the MSMA prototype.

Language policy: all user-facing wording is taken verbatim from Halle's
MSMA documentation and the GCS Mentee Decision Tree crosswalk. Where the
doc marks something as still to be written (e.g. the Section 5 summary),
the app shows a placeholder rather than invented text.
"""

MARK = open("/tmp/logo_mark.txt").read().strip()
WORD = open("/tmp/logo_word.txt").read().strip()

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mentee Skill Matching Assessment (MSMA)</title>
<style>
  :root{
    --ink:#1f2a28; --muted:#5f6f6b; --faint:#8aa09a;
    --teal:#0f6e56; --teal-mid:#1d9e75; --teal-soft:#e1f5ee;
    --amber:#b97515; --amber-soft:#faeeda;
    --line:#dce6e3; --card:#ffffff; --bg:#f6faf8;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; background:var(--bg); color:var(--ink); line-height:1.6;}
  .wrap{max-width:760px; margin:0 auto; padding:40px 20px 60px;}
  .brand{display:flex; align-items:center; justify-content:center; gap:13px; margin-bottom:16px;}
  .brand-mark{height:50px; width:auto;}
  .brand-word{height:31px; width:auto;}
  @media(max-width:480px){.brand-mark{height:42px;} .brand-word{height:26px;}}
  h1{font-size:25px; font-weight:600; text-align:center;}
  .sub{text-align:center; color:var(--muted); font-size:15px; margin-top:8px;}
  .center{text-align:center;}
  .card{background:var(--card); border:1px solid var(--line); border-radius:14px; padding:26px 28px; margin-top:24px;}
  .btn{display:inline-block; font-size:15px; font-weight:500; color:#fff; background:var(--teal); border:none; border-radius:10px; padding:12px 26px; cursor:pointer; margin-top:18px;}
  .btn.ghost{background:transparent; color:var(--teal); border:1px solid var(--line);}
  .btn:hover{opacity:.92;} .btn:disabled{opacity:.4; cursor:not-allowed;}
  .btn.sm{font-size:13px; padding:8px 16px; margin-top:8px;}
  .opt{display:block; width:100%; text-align:left; font-size:15px; background:#fff; border:1px solid var(--line); border-radius:10px; padding:13px 16px; margin-top:10px; cursor:pointer; color:var(--ink);}
  .opt:hover{border-color:var(--teal-mid); background:var(--teal-soft);}
  .back{background:none; border:none; color:var(--faint); font-size:13px; cursor:pointer; margin-top:14px;}
  .domain{font-size:12px; color:var(--teal); text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;}
  .q{font-size:17px; font-weight:500; line-height:1.5;}
  .chip{font-size:12px; padding:2px 10px; border-radius:999px; display:inline-block;}
  .chip.high{background:var(--teal-soft); color:var(--teal);}
  .chip.partial{background:#eaf3de; color:#3b6d11;}
  .chip.low{background:var(--amber-soft); color:var(--amber);}
  .chip.done{background:var(--teal-soft); color:var(--teal);}
  .chip.wait{background:#eef1f0; color:var(--faint);}
  .mini{background:var(--bg); border-radius:10px; padding:14px 16px; font-size:13.5px; margin-top:12px;}
  .mini h4{font-size:13px; margin-bottom:6px; color:var(--teal);}
  .mini p{color:var(--muted); line-height:1.55;}
  .placeholder{border:1px dashed var(--line); background:transparent; border-radius:10px; padding:14px 16px; margin-top:12px; font-size:13.5px; color:var(--faint); line-height:1.55;}
  .note{font-size:12.5px; color:var(--faint); margin-top:16px; line-height:1.5;}
  .compass{font-size:13.5px; background:var(--teal-soft); color:var(--teal); border-radius:10px; padding:12px 16px; margin-top:16px;}
  .refer{font-size:13px; background:var(--amber-soft); color:#7a4d0c; border-radius:10px; padding:12px 16px; margin-top:14px; line-height:1.5;}
  table{width:100%; border-collapse:collapse; font-size:13px; margin-top:12px;}
  th{font-weight:500; color:var(--muted); text-align:left; padding:8px 6px; border-bottom:1px solid var(--line); font-size:12px;}
  td{padding:9px 6px; border-bottom:1px solid var(--line); vertical-align:top;}
  .hidden{display:none;}
  h2{font-size:19px; font-weight:600;}
  h3{font-size:15px; font-weight:600; margin-top:22px;}
  .field{display:block; width:100%; font-size:14px; border:1px solid var(--line); border-radius:8px; padding:10px 12px; margin-top:8px; background:#fff; color:var(--ink); font-family:inherit;}
  .picks{margin-top:8px;}
  .pickgroup{margin-top:18px;}
  .pickgroup h4{font-size:12px; color:var(--teal); text-transform:uppercase; letter-spacing:1px; margin-bottom:8px;}
  .pick{display:flex; align-items:center; gap:10px; width:100%; text-align:left; font-size:14.5px; background:#fff; border:1px solid var(--line); border-radius:10px; padding:11px 14px; margin-top:8px; cursor:pointer; color:var(--ink); line-height:1.4;}
  .pick:hover{border-color:var(--teal-mid); background:var(--teal-soft);}
  .pick.on{border-color:var(--teal-mid); background:var(--teal-soft);}
  .pick .rank{flex:0 0 22px; height:22px; border-radius:50%; border:1px solid var(--line); font-size:12px; display:flex; align-items:center; justify-content:center; color:var(--faint); background:#fff;}
  .pick.on .rank{background:var(--teal); color:#fff; border-color:var(--teal); font-weight:600;}
  .tally{position:sticky; bottom:0; background:var(--card); border-top:1px solid var(--line); padding:14px 0 4px; margin-top:20px;}
  .linkbox{background:var(--bg); border:1px solid var(--line); border-radius:10px; padding:12px 14px; margin-top:10px; font-size:12.5px; word-break:break-all; color:var(--muted);}
  .linkbox b{color:var(--ink); font-size:13px; display:block; margin-bottom:4px;}
  .status{display:flex; gap:8px; flex-wrap:wrap; margin-top:12px;}
  footer{text-align:center; font-size:12px; color:var(--faint); margin-top:36px; line-height:1.6;}
  @media print{ body{background:#fff;} .no-print{display:none !important;} .card{border:none; padding:6px 0;} }
</style>
</head>
<body>
<div class="wrap">
  <div class="brand">
    <img class="brand-mark" src="__MARK__" alt="">
    <img class="brand-word" src="__WORD__" alt="YESS Lab">
  </div>
  <h1>Mentee Skill Matching Assessment (MSMA)</h1>
  <p class="sub">Integrated School Mentoring &bull; YESS Lab &bull; University of South Carolina</p>

  <!-- LANDING -->
  <div id="screen-landing" class="card">
    <p style="color:var(--muted); font-size:15px;">The purpose of the MSMA is to translate a mentee&rsquo;s identified needs into the specific mentoring skills that can become the focus of the mentoring relationship. This assessment is to be completed after the Top Needs Assessment by the school team, counselor, social worker, or mentoring coordinator.</p>
    <h3>Who is responding?</h3>
    <button class="opt" onclick="setRole('caregiver')">Caregiver</button>
    <button class="opt" onclick="setRole('teacher')">Teacher</button>
    <button class="opt" onclick="setRole('mentee')">Mentee</button>
    <button class="opt" onclick="setRole('coordinator')">School team / mentoring coordinator</button>
    <p class="note">In use, each respondent opens their own link and does not see this screen. This picker exists so the full assessment can be demonstrated from one device.</p>
  </div>

  <!-- RESPONDENT: CODE -->
  <div id="screen-r-start" class="card hidden">
    <p class="domain" id="r-role-label"></p>
    <h2>Section 1: Compile Top Needs</h2>
    <p style="margin-top:8px; color:var(--muted); font-size:14.5px;">Enter the case code from your invitation to begin.</p>
    <input class="field" id="r-code" placeholder="Case code" oninput="rReady()">
    <div class="center"><button class="btn" id="r-go" onclick="go('r-pick')" disabled>Continue</button></div>
    <button class="back no-print" onclick="go('landing')">&#8592; Back</button>
  </div>

  <!-- RESPONDENT: PICK -->
  <div id="screen-r-pick" class="card hidden">
    <p class="domain" id="p-role-label"></p>
    <h2>Enter the Top Needs identified</h2>
    <p style="margin-top:8px; color:var(--muted); font-size:14.5px;">Select Need #1 first, then Need #2 and Need #3 if applicable.</p>
    <div class="picks" id="pickbox"></div>
    <div class="tally">
      <p style="font-size:13.5px;" id="tally-text">Nothing selected yet.</p>
      <div class="center"><button class="btn" id="p-submit" onclick="submitResponse()" disabled>Submit</button></div>
    </div>
    <button class="back no-print" onclick="go('r-start')">&#8592; Back</button>
  </div>

  <!-- RESPONDENT: DONE -->
  <div id="screen-r-done" class="card hidden">
    <h2>Response recorded</h2>
    <p style="margin-top:10px; color:var(--muted); font-size:15px;">Your Top Needs have been recorded. The school team will compile the responses from each member.</p>
    <div class="center no-print"><button class="btn ghost" onclick="location.href=location.pathname">Return to start</button></div>
  </div>

  <!-- COORDINATOR HUB -->
  <div id="screen-c-hub" class="card hidden">
    <p class="domain">School team</p>
    <h2>Section 1: Compile Top Needs</h2>
    <p style="margin-top:8px; color:var(--muted); font-size:14.5px;">Enter a case code, then share the links below with each member. Responses appear here as they are received.</p>
    <input class="field" id="c-code" placeholder="Case code" oninput="renderHub()">
    <div id="hub-body"></div>
    <button class="back no-print" onclick="go('landing')">&#8592; Back</button>
  </div>

  <!-- DECISION QUESTIONS -->
  <div id="screen-c-dq" class="card hidden">
    <p class="domain">Section 3</p>
    <h2>Decision Questions</h2>
    <p style="margin-top:8px; color:var(--muted); font-size:14px;">These questions are answered if all three members differ in their Top Need.</p>
    <div id="dq-list" class="note" style="margin-top:10px;"></div>
    <div id="dq-body" style="margin-top:18px;"></div>
    <button class="back no-print" onclick="restartDQ()">&#8592; Start Decision Questions over</button>
  </div>

  <!-- RESULTS -->
  <div id="screen-c-results" class="card hidden">
    <p class="domain">The Results</p>
    <h2 id="res-head">Section 3: Determine the Primary Underlying Skill</h2>
    <p style="color:var(--muted); font-size:14px; margin-top:6px;">Skill Convergence: The MSMA compares the identified concerns against the mentoring skill crosswalk to determine whether different concerns reflect the same underlying developmental skill needs.</p>
    <div class="compass" id="conv-box"></div>
    <div id="refer-box"></div>

    <h3>Section 2: Identify Patterns</h3>
    <p style="font-size:13.5px; color:var(--muted); margin-top:4px;" id="pattern-line"></p>

    <h3>Section 4: Needs Convergence Matrix</h3>
    <table id="matrix"></table>
    <p class="note">Columns auto-populate the needs, skill, and recommendation. Priority is populated as High, Partial, or Low depending on the Skill convergence.</p>

    <h3>Section 5: Summary</h3>
    <div id="summary"></div>

    <div class="center no-print">
      <button class="btn ghost" onclick="copyResults(this)">Copy results</button>
      <button class="btn ghost" onclick="window.print()">Save (PDF)</button>
    </div>
    <div class="center no-print"><button class="btn ghost" onclick="go('c-hub')">&#8592; Back to responses</button></div>
  </div>

  <footer>MSMA draft prototype, in development with the YESS Lab mentoring team.<br>Concern list and skill crosswalk from the MSMA documentation and the GCS Mentee Decision Tree.</footer>
</div>

<script>
/* ---------------------------------------------------------------
   SKILL GROUPS
   Convergence requires concerns to be comparable, so the crosswalk's
   per-concern skill wording is grouped. Group names use the doc's own
   terms where the doc names them (Emotion Regulation, Executive
   Functioning / Time management, Confidence Building) and the
   crosswalk's Underlying Skill Need wording otherwise.
   --------------------------------------------------------------- */
const SKILLS = {
  ef:   "Executive Functioning / Time management",
  acad: "Learning strategies / Study habits",
  goal: "Goal setting, self-efficacy",
  emot: "Emotion Regulation",
  well: "Emotional wellness",
  conf: "Confidence Building",
  comm: "Communication and empathy",
  cres: "Conflict resolution"
};

/* Crosswalk: GCS Mentee Decision Tree (verbatim) */
const CONCERNS = [
  {label:"Incomplete work",            domain:"Academic",   skill:"ef",   need:"Task initiation, planning, time management", res:"Time Management, Task Planning, Goal Setting"},
  {label:"Grade dropping",             domain:"Academic",   skill:"acad", need:"Study habits, academic engagement",          res:"Study Skills, Academic Success Strategies, Growth Mindset"},
  {label:"Poor study habits",          domain:"Academic",   skill:"acad", need:"Learning strategies",                        res:"Study Skills, Note Taking, Test Preparation"},
  {label:"Missing assignments",        domain:"Academic",   skill:"ef",   need:"Organization, accountability",               res:"Organization, Planner Systems, Time Management"},
  {label:"Low academic motivation",    domain:"Academic",   skill:"goal", need:"Goal setting, self-efficacy",                res:"Goal Setting, Motivation, Growth Mindset"},
  {label:"Organization",               domain:"Behavioral", skill:"ef",   need:"Executive functioning",                      res:"Organization Systems, Executive Function Skills"},
  {label:"Procrastination",            domain:"Behavioral", skill:"ef",   need:"Task initiation, prioritization",            res:"Prioritization, Time Blocking, Breaking Tasks into Steps"},
  {label:"Poor time management",       domain:"Behavioral", skill:"ef",   need:"Planning and scheduling",                    res:"Time Management, Routine Building"},
  {label:"Poor attendance",            domain:"Behavioral", skill:"goal", need:"Habits, accountability",                     res:"Habit Building, Accountability, Goal Setting"},
  {label:"Difficulty staying focused", domain:"Behavioral", skill:"ef",   need:"Attention and self-management",              res:"Self-Regulation, Focus Strategies, Executive Function Skills"},
  {label:"Stress",                     domain:"Emotional",  skill:"emot", need:"Coping strategies",                          res:"Stress Management, Mindfulness, Relaxation Techniques"},
  {label:"Anxiety",                    domain:"Emotional",  skill:"emot", need:"Emotional regulation",                       res:"Coping Skills, Emotional Regulation, Mindfulness"},
  {label:"Sadness/Depression",         domain:"Emotional",  skill:"well", need:"Emotional wellness",                         res:"Emotional Wellness, Resilience, Self-Care", refer:true},
  {label:"Low self-confidence",        domain:"Emotional",  skill:"conf", need:"Self-efficacy",                              res:"Confidence Building, Strengths-Based Coaching, Positive Self-Talk"},
  {label:"Feeling overwhelmed",        domain:"Emotional",  skill:"emot", need:"Prioritization and coping",                  res:"Stress Management, Organization, Resilience"},
  {label:"Relationship struggles",     domain:"Social",     skill:"comm", need:"Communication and empathy",                  res:"Communication Skills, Healthy Relationships, Emotional Intelligence"},
  {label:"Conflict with peers",        domain:"Social",     skill:"cres", need:"Conflict resolution",                        res:"Conflict Resolution, Active Listening, Problem Solving"},
  {label:"Difficulty making friends",  domain:"Social",     skill:"comm", need:"Social skills",                              res:"Relationship Building, Social Skills, Communication"},
  {label:"Poor communication",         domain:"Social",     skill:"comm", need:"Interpersonal effectiveness",                res:"Communication Skills, Active Listening, Assertiveness"}
];

const DOMAIN_ORDER = ["Social","Emotional","Behavioral","Academic"];
const ROLES = {caregiver:"Caregiver", teacher:"Teacher", mentee:"Mentee"};
const ROLE_ORDER = ["caregiver","teacher","mentee"];

/* Section 2 statements, verbatim */
const PATTERNS = {
  High:    "All three members identified essentially the same primary concern",
  Partial: "Two sources agreed on the primary concern",
  Low:     "All three sources identified different concerns"
};

let role=null, picks=[], state={};
const MEM = {};
const KEY = c => "msma:" + c.trim().toUpperCase();
function load(c){ try{ return JSON.parse(localStorage.getItem(KEY(c))) || MEM[KEY(c)] || {}; }catch(e){ return MEM[KEY(c)] || {}; } }
function save(c,d){ MEM[KEY(c)] = d; try{ localStorage.setItem(KEY(c), JSON.stringify(d)); }catch(e){} }
function concernBy(l){ return CONCERNS.find(c => c.label === l); }

function go(name){
  ["landing","r-start","r-pick","r-done","c-hub","c-dq","c-results"].forEach(s =>
    document.getElementById("screen-"+s).classList.toggle("hidden", s !== name));
  if (name==="r-pick") renderPicks();
  if (name==="c-hub")  renderHub();
  window.scrollTo(0,0);
}

(function initFromURL(){
  const p = new URLSearchParams(location.search), r = p.get("role"), c = p.get("code");
  if (r && ROLES[r]){ role=r; if(c) document.getElementById("r-code").value=c;
    setRoleScreens(); go(c ? "r-pick" : "r-start"); rReady(); }
  else if (r === "coordinator"){ role="coordinator"; if(c) document.getElementById("c-code").value=c; go("c-hub"); }
})();

function setRole(r){ role=r; if(r==="coordinator"){go("c-hub");return;} setRoleScreens(); go("r-start"); }
function setRoleScreens(){
  document.getElementById("r-role-label").textContent = ROLES[role];
  document.getElementById("p-role-label").textContent = ROLES[role];
}
function rReady(){ document.getElementById("r-go").disabled = !document.getElementById("r-code").value.trim(); }

/* ---- Need Responses (Drop Down list) ---- */
function renderPicks(){
  picks = [];
  const box = document.getElementById("pickbox"); box.innerHTML = "";
  DOMAIN_ORDER.forEach(d => {
    const g = document.createElement("div"); g.className="pickgroup";
    g.innerHTML = "<h4>"+d+"</h4>";
    CONCERNS.filter(c=>c.domain===d).forEach(c => {
      const b=document.createElement("button"); b.className="pick"; b.dataset.label=c.label;
      b.innerHTML = "<span class='rank'></span><span>"+c.label+"</span>";
      b.onclick = () => togglePick(c.label);
      g.appendChild(b);
    });
    box.appendChild(g);
  });
  updateTally();
}
function togglePick(l){
  const i = picks.indexOf(l);
  if (i>-1) picks.splice(i,1); else if (picks.length<3) picks.push(l);
  updateTally();
}
function updateTally(){
  document.querySelectorAll(".pick").forEach(b=>{
    const i = picks.indexOf(b.dataset.label);
    b.classList.toggle("on", i>-1);
    b.querySelector(".rank").textContent = i>-1 ? (i+1) : "";
  });
  const t = document.getElementById("tally-text");
  t.innerHTML = picks.length
    ? "<b>Need #1:</b> " + picks.map((l,i)=>(i?"&nbsp; <b>Need #"+(i+1)+":</b> ":"")+l).join("")
    : "Nothing selected yet.";
  document.getElementById("p-submit").disabled = picks.length===0;
}
function submitResponse(){
  const code = document.getElementById("r-code").value.trim();
  const d = load(code);
  d[role] = {needs: picks.slice()};
  save(code, d);
  go("r-done");
}

/* ---- coordinator hub ---- */
function renderHub(){
  const code = document.getElementById("c-code").value.trim();
  const box = document.getElementById("hub-body");
  if (!code){ box.innerHTML=""; return; }
  const d = load(code), base = location.origin + location.pathname;
  let html = "<h3>Links to share</h3>";
  html += "<p class='note' style='margin-top:4px;'><b>Prototype note:</b> responses are stored in this browser only and do not sync across devices. To walk the full assessment, open all three links on this device.</p>";
  ROLE_ORDER.forEach(r=>{
    const url = base+"?role="+r+"&code="+encodeURIComponent(code.toUpperCase());
    html += "<div class='linkbox'><b>"+ROLES[r]+"</b>"+url+
      "<br><button class='btn ghost sm no-print' onclick=\"copyText('"+url.replace(/'/g,"\\'")+"', this)\">Copy link</button></div>";
  });
  html += "<h3>Responses received</h3><div class='status'>";
  ROLE_ORDER.forEach(r=>{
    const got = d[r] && d[r].needs && d[r].needs.length;
    html += "<span class='chip "+(got?"done":"wait")+"'>"+ROLES[r]+(got?" &#10003;":" pending")+"</span>";
  });
  html += "</div>";
  const have = ROLE_ORDER.filter(r=>d[r]&&d[r].needs&&d[r].needs.length);
  if (have.length){
    html += "<table><tr><th></th><th>Need #1</th><th>Need #2</th><th>Need #3</th></tr>";
    have.forEach(r=>{
      const n=d[r].needs;
      html += "<tr><td><b>"+ROLES[r]+"</b></td><td>"+(n[0]||"&mdash;")+"</td><td>"+(n[1]||"&mdash;")+"</td><td>"+(n[2]||"&mdash;")+"</td></tr>";
    });
    html += "</table>";
  }
  html += "<div class='center'><button class='btn' "+(have.length<2?"disabled":"")+" onclick='runMatch()'>Determine Primary Underlying Skill</button></div>";
  if (have.length && have.length<3)
    html += "<p class='note center'>"+(3-have.length)+" response(s) pending.</p>";
  html += "<div class='center no-print'><button class='btn ghost sm' onclick='clearCode()'>Clear responses for this case</button></div>";
  box.innerHTML = html;
}
function clearCode(){
  const c = document.getElementById("c-code").value.trim();
  if (c && confirm("Clear all stored responses for "+c.toUpperCase()+"?")){ localStorage.removeItem(KEY(c)); delete MEM[KEY(c)]; renderHub(); }
}
function copyText(t, btn){
  const done=()=>{const o=btn.textContent; btn.textContent="Copied"; setTimeout(()=>btn.textContent=o,1500);};
  if (navigator.clipboard) navigator.clipboard.writeText(t).then(done).catch(()=>fallbackCopy(t,done)); else fallbackCopy(t,done);
}

/* ---- Section 3: skill convergence ---- */
function runMatch(){
  const code = document.getElementById("c-code").value.trim(), d = load(code);
  const respondents = ROLE_ORDER.filter(r=>d[r]&&d[r].needs&&d[r].needs.length).map(r=>({
    key:r, source:ROLES[r], primary:concernBy(d[r].needs[0]), extras:d[r].needs.slice(1)
  }));
  const tally={}; respondents.forEach(p=>tally[p.primary.skill]=(tally[p.primary.skill]||0)+1);
  const ranked = Object.entries(tally).sort((a,b)=>b[1]-a[1]);
  const top = ranked[0][1], n = respondents.length;
  state = {code, picks:respondents, dq:{}};
  if (top===n){ state.level="High";    state.primarySkill=ranked[0][0]; state.secondarySkill=null; }
  else if (top>=2){ state.level="Partial"; state.primarySkill=ranked[0][0]; state.secondarySkill=ranked[1][0]; }
  else { state.level="Low"; return startDQ(); }
  showResults();
}

/* ---- Decision Questions (verbatim) ---- */
function startDQ(){
  state.dq={}; go("c-dq");
  document.getElementById("dq-list").innerHTML =
    state.picks.map(p=>p.source+" &rarr; "+p.primary.label).join("<br>");
  renderDQ(1);
}
function restartDQ(){ startDQ(); }
function dqOptions(q,list,next){
  const box=document.getElementById("dq-body");
  box.innerHTML = "<p class='q'>"+q+"</p>";
  list.forEach(o=>{const b=document.createElement("button"); b.className="opt"; b.innerHTML=o.text; b.onclick=()=>next(o.value); box.appendChild(b);});
  window.scrollTo(0,0);
}
function sourceOpts(){ return state.picks.map(p=>({value:p.key, text:p.source+" Top Need &mdash; "+p.primary.label})); }
function renderDQ(n){
  if (n===1) dqOptions("1. &ldquo;What concern currently causes the greatest impairment?&rdquo;",
    DOMAIN_ORDER.map(d=>({value:d, text:d+" Functioning"})), v=>{state.dq.impairment=v; renderDQ(2);});
  else if (n===2) dqOptions("2. &ldquo;What concern is most likely to prevent success within mentoring if left unaddressed?&rdquo;",
    sourceOpts(), v=>{state.dq.q2=v; renderDQ(3);});
  else if (n===3) dqOptions("3. &ldquo;Which concern is most developmentally appropriate for mentoring?&rdquo;",
    sourceOpts().concat([{value:"combination", text:"Combination"}]),
    v=>{ state.dq.q3=v; if (v!=="combination" && v===state.dq.q2) resolveDQ([state.dq.q2]); else renderDQ(4); });
  else if (n===4) dqOptions("&ldquo;Do these concerns point to similar underlying needs?&rdquo;",
    [{value:"yes", text:"Yes &mdash; primary focus as both, with overlapping skills"},
     {value:"no",  text:"No"}],
    v=>{ state.dq.similar=v;
      if (v==="yes") resolveDQ(state.dq.q3==="combination" ? state.picks.map(p=>p.key) : [state.dq.q2,state.dq.q3]);
      else renderDQ(5); });
  else if (n===5) dqOptions("&ldquo;Which concern is affecting the student most across settings?&rdquo;",
    sourceOpts(), v=>{ state.dq.across=v; resolveDQ([v]); });
}
function resolveDQ(keys){
  const chosen = keys.map(k=>state.picks.find(p=>p.key===k));
  state.primarySkill = chosen[0].primary.skill;
  state.secondarySkill = chosen.length>1 ? chosen[1].primary.skill : null;
  if (state.secondarySkill===state.primarySkill) state.secondarySkill=null;
  showResults();
}

/* ---- Results ---- */
let resultLines=[];
function showResults(){
  go("c-results");
  const lvl=state.level, cls=lvl.toLowerCase();
  const defn = {
    High:   "The concerns map to the same mentoring skills. Respondents may have identified different concerns, but these concerns map to the same mentoring skill area.",
    Partial:"The concern maps to two related mentoring skills.",
    Low:    "The concerns map to three distinct mentoring skill areas."
  }[lvl];
  const pri = SKILLS[state.primarySkill], sec = state.secondarySkill ? SKILLS[state.secondarySkill] : null;

  document.getElementById("conv-box").innerHTML =
    "<span class='chip "+cls+"'>"+lvl+" Convergence</span><br><span style='color:var(--muted)'>"+defn+"</span><br><br>" +
    (sec ? "<b>Primary Skill:</b> "+pri+"<br><b>Secondary Skill:</b> "+sec
         : "<b>Underlying Skill:</b> "+pri);

  document.getElementById("pattern-line").textContent = PATTERNS[lvl];

  const flagged = state.picks.filter(p=>p.primary.refer);
  document.getElementById("refer-box").innerHTML = flagged.length
    ? "<div class='refer'>Sadness/Depression identified by "+flagged.map(p=>p.source).join(", ")+
      ". The crosswalk notes referral if indicated.</div>" : "";

  const tbl=document.getElementById("matrix");
  tbl.innerHTML="<tr><th>Source</th><th>Need Identified</th><th>Underlying Skill</th><th>Priority</th><th>Recommendation</th></tr>";
  state.picks.forEach(p=>{
    const extras = p.extras.length ? "<br><span style='color:var(--faint); font-size:12px;'>"+p.extras.join(", ")+"</span>" : "";
    tbl.innerHTML += "<tr><td><b>"+p.source+"</b></td><td>"+p.primary.label+extras+"</td><td>"+p.primary.need+
      "</td><td><span class='chip "+cls+"'>"+lvl+"</span></td><td>"+p.primary.res+"</td></tr>";
  });

  const resList = [...new Set(state.picks.filter(p=>p.primary.skill===state.primarySkill).flatMap(p=>p.primary.res.split(", ")))];
  document.getElementById("summary").innerHTML =
    "<div class='placeholder'>A summary will be populated based on the recommended skill and what that might specifically look like. If resources are applicable for the skills, those will be linked as well.<br><br><i>Summary text to be written.</i></div>" +
    "<div class='mini'><h4>Recommended Training/Skills</h4><p>"+resList.join(" &bull; ")+"</p></div>";

  resultLines = ["Mentee Skill Matching Assessment (MSMA)", "Case "+state.code.toUpperCase(), "",
                 lvl+" Convergence", defn, ""];
  state.picks.forEach(p=>resultLines.push("  "+p.source+": "+p.primary.label+" -> "+p.primary.need));
  resultLines.push("", sec ? "Primary Skill: "+pri+"\nSecondary Skill: "+sec : "Underlying Skill: "+pri);
  resultLines.push("", "Recommended Training/Skills: "+resList.join(", "));
  if (flagged.length) resultLines.push("", "Sadness/Depression identified. Crosswalk notes referral if indicated.");
}

function copyResults(btn){ copyText(resultLines.join("\n"), btn); }
function fallbackCopy(text, done){
  const ta=document.createElement("textarea"); ta.value=text; document.body.appendChild(ta); ta.select();
  try{document.execCommand("copy");}catch(e){} document.body.removeChild(ta); done();
}
</script>
</body>
</html>
"""

HTML = HTML.replace("__MARK__", MARK).replace("__WORD__", WORD)
open("index.html", "w", encoding="utf-8").write(HTML)
print("built index.html (%.0f KB)" % (len(HTML.encode())/1024))
