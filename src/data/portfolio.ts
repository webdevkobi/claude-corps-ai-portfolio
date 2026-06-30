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
    title: "Starts with the real workflow",
    text: "I talk to people, watch the process, and find where time or attention is leaking before deciding what to build.",
    icon: ClipboardCheck,
  },
  {
    title: "Builds tools people actually use",
    text: "Dashboards, automations, private apps, integrations, and feedback loops are only useful if they make the day easier.",
    icon: Bot,
  },
  {
    title: "Explains without making people feel small",
    text: "I can teach students, athletes, founders, and nontechnical users because I care more about whether it lands than how fancy it sounds.",
    icon: GraduationCap,
  },
  {
    title: "Leaves something someone can own",
    text: "The goal is not for people to need me forever. The goal is a tool, habit, or workflow they can keep using after I leave.",
    icon: ShieldCheck,
  },
];

export const caseStudies: CaseStudy[] = [
  {
    id: "content-system",
    title: "Champions Voice Content OS",
    eyebrow: "Weekly review into weekly action",
    image: "content-system.png",
    alt: "Redacted Notion captures showing a weekly content calendar, content matrix, performance review, and next-week iteration brief.",
    stack: ["Notion", "Claude", "ChatGPT", "Instagram analytics", "Human review"],
    metric: "20K+ followers in two months",
    summary:
      "Every week I look at what worked, what missed, and what young athletes actually responded to. Then I use AI to turn those notes into the next week of content while I keep the final judgment.",
    problem:
      "I was trying to build something that could help thousands of student-athletes, but planning everything manually made it too easy to miss patterns or repeat the wrong thing.",
    shipped: [
      "Built a weekly Notion system for content ideas, hooks, formats, CTAs, analytics, and audience feedback.",
      "Created a human-in-the-loop review where I decide what actually mattered before AI helps build the next week.",
      "Used outlier posts, including 250K+ and 500K+ view formats, to shape the next experiments instead of guessing.",
    ],
    handoff:
      "A teammate could open the calendar, see the week, understand why posts worked, and keep the loop going without needing to guess how I think.",
    signal:
      "This is the same muscle Claude Corps needs: learn the actual workflow, build with AI, keep judgment in the room, and teach the system.",
    icon: ChartNoAxesCombined,
  },
  {
    id: "lead-funnel",
    title: "ManyChat to Notion Lead Capture Funnel",
    eyebrow: "Audience to owned relationship",
    image: "lead-funnel.png",
    alt: "Redacted Notion client list showing the ManyChat to Notion lead system with private emails blurred.",
    stack: ["ManyChat", "Notion", "Instagram DMs", "Client database", "Automation"],
    metric: "1,500+ emails collected in two months",
    summary:
      "The audience was not just views. People raised their hand, gave me an email, and became someone I could actually follow up with and help.",
    problem:
      "Instagram attention disappears fast. I needed a real client list so interest from DMs could become owned relationships instead of getting lost.",
    shipped: [
      "Connected DM-driven calls-to-action to email capture and a Notion client list.",
      "Tracked names, lead status, source, latest interaction, and follow-up context in one place.",
      "Redacted private emails in the public portfolio while still showing the actual system shape.",
    ],
    handoff:
      "The owner sees the client list, understands what each field is for, and has one clear place to check follow-up instead of hunting through DMs.",
    signal:
      "Shows the kind of practical integration a host organization may need: take real interest from people and turn it into follow-up that does not get dropped.",
    icon: Users,
  },
  {
    id: "training-app",
    title: "Private Driveline Training App",
    eyebrow: "Source-faithful personal AI tool",
    image: "training-app.png",
    alt: "Redacted Driveline Trainer dashboard screenshot showing home, coach build, calendar, and workout library navigation.",
    stack: ["Node.js", "Vercel", "Blob storage", "Mobile web", "Data cleanup"],
    metric: "Two years of training history made usable",
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
      "The next owner can see how to run it, what data it trusts, and what the app is not allowed to make up.",
    signal:
      "Demonstrates end-to-end product judgment: private data boundaries, mobile usability, and practical AI-assisted planning.",
    icon: Code2,
  },
  {
    id: "daily-brief",
    title: "Daily Inbox Brief",
    eyebrow: "Morning triage dashboard",
    image: "daily-brief.png",
    alt: "Redacted daily inbox brief screenshot with brand deals, opportunities, drafts ready, and blurred email details.",
    stack: ["HTML", "CSS", "JavaScript", "Gmail links", "Scheduled desktop automation"],
    metric: "Daily need-to-know brief before the day starts",
    summary:
      "A morning dashboard that pulls the important inbox context forward so I can start the day with signal instead of sorting through noise.",
    problem:
      "Important business opportunities were mixed with low-value inbox volume, which meant attention was getting spent before the real work even started.",
    shipped: [
      "Built a polished local brief that opens each morning with priority counts, reasons, direct thread links, and suggested next action.",
      "Packaged the workflow as a scheduled desktop task rather than a fragile one-off script.",
      "Kept sensitive names and email addresses redacted in the public portfolio evidence.",
    ],
    handoff:
      "The dashboard explains what matters and why, so someone else could follow the morning rhythm without learning the whole inbox first.",
    signal:
      "This is the kind of small but high-leverage automation Claude Corps hosts often need: not flashy, just useful every day.",
    icon: MailCheck,
  },
  {
    id: "shopify-ops",
    title: "Champions Voice Landing Page and Web Ops",
    eyebrow: "Public front door for the work",
    image: "shopify-ops.png",
    alt: "Champions Voice landing page screenshot showing the public storefront hero.",
    stack: ["Shopify", "GitHub", "Landing page QA", "Accessibility", "Content ops"],
    metric: "Storefront work kept in a review-first flow",
    summary:
      "The site is the public front door for Champions Voice. I used AI to help audit, improve, and document the work while keeping final judgment on what should ship.",
    problem:
      "The brand needed a cleaner path from attention to waitlist and products without accidentally pushing unfinished changes live.",
    shipped: [
      "Audited CTA paths, mobile layout, empty states, headings, and accessibility details.",
      "Used AI as a second set of eyes for changes that were tedious to check manually.",
      "Stopped deployment when the supposed sandbox theme turned out to be live.",
    ],
    handoff:
      "Someone taking over can see what was checked, what changed, and when not to push live.",
    signal:
      "Shows judgment under constraints: sometimes the right technical move is telling someone not to ship yet.",
    icon: Store,
  },
];

export const operatingPrinciples = [
  {
    title: "I build around my attention",
    text: "I know I can only put my full attention in so many places. AI helps me build systems so important things do not fall through the holes.",
    icon: BookOpenCheck,
  },
  {
    title: "Small tools count",
    text: "A morning brief, a tracker, or a client list can change the whole day when it removes a tedious task from my brain.",
    icon: PanelsTopLeft,
  },
  {
    title: "AI gives me autonomy",
    text: "It lets me decide how I want to spend my day instead of letting admin work decide for me.",
    icon: Handshake,
  },
  {
    title: "I still stay in the loop",
    text: "AI can sort, summarize, and draft. I still make the judgment calls, especially when people are involved.",
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
