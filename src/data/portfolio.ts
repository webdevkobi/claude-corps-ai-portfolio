import type { LucideIcon } from "lucide-react";
import {
  ArrowUpRight,
  BookOpenCheck,
  Bot,
  ChartNoAxesCombined,
  ClipboardCheck,
  Code2,
  GraduationCap,
  Handshake,
  MailCheck,
  PanelsTopLeft,
  ShieldCheck,
  Store,
  Users,
  Wrench,
} from "lucide-react";

export type FitSignal = {
  title: string;
  text: string;
  icon: LucideIcon;
};

export type CaseStudy = {
  id: string;
  title: string;
  eyebrow: string;
  image: string;
  alt: string;
  stack: string[];
  metric: string;
  summary: string;
  problem: string;
  shipped: string[];
  handoff: string;
  signal: string;
  icon: LucideIcon;
};

export const fitSignals: FitSignal[] = [
  {
    title: "Discovers before building",
    text: "Turns vague workflow pain into concrete sprints, inputs, success checks, and owner-ready next actions.",
    icon: ClipboardCheck,
  },
  {
    title: "Builds usable AI systems",
    text: "Ships dashboards, automations, private apps, integrations, and feedback loops with Claude, Codex, Notion, APIs, and web tooling.",
    icon: Bot,
  },
  {
    title: "Teaches mixed rooms",
    text: "Explains systems to students, athletes, founders, and nontechnical users without making the tool the point.",
    icon: GraduationCap,
  },
  {
    title: "Hands off cleanly",
    text: "Documents guardrails, runbooks, source-of-truth rules, and deployment holds so someone else can safely own the system.",
    icon: ShieldCheck,
  },
];

export const caseStudies: CaseStudy[] = [
  {
    id: "content-system",
    title: "Champions Voice AI Content Operating System",
    eyebrow: "Human-in-the-loop growth engine",
    image: "content-system.png",
    alt: "Sanitized capture of a Notion-style content operating system with weekly analytics and next-week planning.",
    stack: ["Notion", "Claude", "ChatGPT Projects", "Instagram analytics", "Weekly evals"],
    metric: "20.7K followers in roughly 2-3 months",
    summary:
      "A weekly operating system that turns content performance into the next plan: post links, analytics, audience comments, human judgment, then AI-generated experiments for the following week.",
    problem:
      "Champions Voice needed a repeatable content engine that preserved Jakobi's voice while moving faster than manual weekly planning.",
    shipped: [
      "Created a Creator Vision source of truth and weekly feedback workflow for hooks, formats, CTAs, and content pillars.",
      "Analyzed weekly performance with a human review layer before asking AI to generate the next 7-day matrix.",
      "Captured learning from outlier posts, including a 250K+ view format that produced about 918 follows in one review cycle.",
    ],
    handoff:
      "The system is understandable as a weekly runbook: collect links, paste analytics, record what landed, generate next-week experiments, then review before publishing.",
    signal:
      "Matches Claude Corps work: evaluation loops, stakeholder judgment, nontechnical ownership, and measurable social-impact reach.",
    icon: ChartNoAxesCombined,
  },
  {
    id: "lead-funnel",
    title: "ManyChat to Notion Lead Capture Funnel",
    eyebrow: "Audience to owned relationship",
    image: "lead-funnel.png",
    alt: "Sanitized capture of an Instagram DM to ManyChat to Notion lead funnel with redacted lead rows.",
    stack: ["ManyChat", "Notion", "Instagram DMs", "Client database", "Automation"],
    metric: "350-400 emails captured in 2-3 weeks",
    summary:
      "A connector that moved Instagram interest into an owned Notion client list with source, email, lead status, latest interaction, and notes.",
    problem:
      "Followers were engaging through rented social platforms, but the business needed a reliable client list that could be followed up and understood.",
    shipped: [
      "Mapped the Notion client-list schema around the real follow-up workflow rather than a generic CRM template.",
      "Connected DM-driven calls-to-action to email capture and Notion records.",
      "Kept personal contact records out of public artifacts while preserving the system architecture for review.",
    ],
    handoff:
      "The handoff surface is a plain-language database schema plus a flow diagram that explains where each field comes from and how to audit a failed capture.",
    signal:
      "Shows the ability to build integrations that make a nonprofit or public-interest team faster without forcing them into a complex new tool.",
    icon: Users,
  },
  {
    id: "training-app",
    title: "Private Driveline Training App",
    eyebrow: "Source-faithful personal AI tool",
    image: "training-app.png",
    alt: "Sanitized capture of a private training app dashboard with source counts and blurred prescription details.",
    stack: ["Node.js", "Vercel", "Blob storage", "Mobile web", "Data cleanup"],
    metric: "402 events, 98 variants, 2,374 exercise rows",
    summary:
      "A mobile and desktop training app built from two years of exported training data. Recommendations select existing source plans instead of inventing workouts.",
    problem:
      "The useful training history was locked inside read-only exports, making it hard to search, repeat, or adapt on the field.",
    shipped: [
      "Converted exported calendar history into a searchable workout library and calendar workflow.",
      "Added readiness check-ins, coach-build flows, completion check-offs, session notes, and cloud sync.",
      "Preserved sets, reps, rest, load, notes, and plan variants so the app stayed source-faithful.",
    ],
    handoff:
      "The README documents local run steps, cloud access assumptions, data fidelity rules, and what the app refuses to invent.",
    signal:
      "Demonstrates end-to-end product judgment: private data boundaries, source truth, mobile usability, and practical AI-assisted planning.",
    icon: Code2,
  },
  {
    id: "daily-brief",
    title: "Daily Inbox Brief",
    eyebrow: "Morning triage dashboard",
    image: "daily-brief.png",
    alt: "Sanitized daily inbox brief with brand deals, opportunities, filtered noise, and redacted email details.",
    stack: ["HTML", "CSS", "JavaScript", "Gmail links", "Scheduled desktop automation"],
    metric: "8:00 AM daily operating rhythm",
    summary:
      "A morning dashboard that classifies inbox threads into brand deals, opportunities, and filtered noise with reasons and next actions.",
    problem:
      "Important business opportunities were mixed with low-value inbox volume, adding daily cognitive overhead before meaningful work started.",
    shipped: [
      "Built a polished local brief that opens each morning with priority counts, reasons, direct thread links, and suggested next action.",
      "Packaged the workflow as a scheduled desktop task rather than a fragile one-off script.",
      "Kept sensitive names and email addresses redacted in the public portfolio evidence.",
    ],
    handoff:
      "The handoff is operational: local files, task schedule, launch script, and a dashboard that explains why each item matters.",
    signal:
      "This is the kind of small but high-leverage automation Claude Corps hosts often need: not flashy, just durable and useful.",
    icon: MailCheck,
  },
  {
    id: "shopify-ops",
    title: "Champions Voice Shopify Web Ops",
    eyebrow: "Safe deployment discipline",
    image: "shopify-ops.png",
    alt: "Sanitized capture of Shopify operations notes with deployment guardrails, QA paths, and theme check status.",
    stack: ["Shopify Liquid", "GitHub", "Theme Check", "Accessibility", "Runbooks"],
    metric: "0 Theme Check errors on latest local batch",
    summary:
      "An AI-assisted website manager workflow for auditing, improving, documenting, and holding changes until a safe sandbox review target exists.",
    problem:
      "The store needed ongoing UX, accessibility, copy, and conversion improvements without accidentally pushing unfinished changes live.",
    shipped: [
      "Audited and fixed CTA paths, search/cart empty states, heading hierarchy, reduced-motion behavior, and mobile overflow issues.",
      "Maintained a daily ops dashboard with blockers, verified paths, shipped changes, and next recommended batch.",
      "Stopped deployment when the supposed sandbox theme was discovered to be live.",
    ],
    handoff:
      "The ops docs define done, review gates, preview paths, and the exact condition that blocks a push.",
    signal:
      "Shows judgment under constraints: sometimes the right technical move is telling a stakeholder not to ship yet.",
    icon: Store,
  },
];

export const operatingPrinciples = [
  {
    title: "Source truth first",
    text: "AI is allowed to accelerate decisions, but important facts live in source systems, docs, schemas, and runbooks.",
    icon: BookOpenCheck,
  },
  {
    title: "Small tools count",
    text: "A dashboard or tracker that reliably saves time is treated as real infrastructure, not a side quest.",
    icon: PanelsTopLeft,
  },
  {
    title: "Enablement is the finish line",
    text: "The work is not done when the tool works; it is done when a real person can own it after handoff.",
    icon: Handshake,
  },
  {
    title: "Judgment beats demos",
    text: "The portfolio includes holds, privacy redactions, and source-faithful constraints because those choices matter in real organizations.",
    icon: Wrench,
  },
];

export const links = [
  {
    label: "Download tailored resume",
    href: `${import.meta.env.BASE_URL}resume/jakobi-davis-claude-corps-resume.pdf`,
    icon: ArrowUpRight,
  },
  {
    label: "Champions Voice",
    href: "https://championsvoice.org/",
    icon: ArrowUpRight,
  },
  {
    label: "GitHub profile",
    href: "https://github.com/webdevkobi",
    icon: ArrowUpRight,
  },
];
