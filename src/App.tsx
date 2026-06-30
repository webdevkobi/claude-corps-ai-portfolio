import {
  ArrowUpRight,
  CheckCircle2,
  ClipboardList,
  Github,
  LockKeyhole,
  Map,
  ShieldCheck,
} from "lucide-react";
import {
  caseStudies,
  fitSignals,
  links,
  operatingPrinciples,
} from "./data/portfolio";

const asset = (name: string) => `${import.meta.env.BASE_URL}assets/${name}`;

function App() {
  return (
    <main>
      <header className="site-header">
        <a className="brand-lockup" href="#top" aria-label="Jakobi Davis portfolio home">
          <span className="brand-mark">JD</span>
          <span>Claude Corps Portfolio</span>
        </a>
        <nav className="top-nav" aria-label="Primary navigation">
          <a href="#case-studies">Case Studies</a>
          <a href="#fit">Fit</a>
          <a href="#handoff">Handoff</a>
        </nav>
      </header>

      <section id="top" className="hero-section">
        <div className="hero-copy">
          <p className="eyebrow">AI workflow builder | educator | founder</p>
          <h1>Jakobi Davis builds the useful AI systems that keep working after the demo.</h1>
          <p className="hero-lede">
            Focused portfolio for Claude Corps: scoped workflows, Claude-assisted builds,
            nontechnical enablement, privacy-aware evidence, and handoff discipline.
          </p>
          <div className="hero-actions" aria-label="Primary links">
            {links.map(({ href, label, icon: Icon }) => (
              <a className="button-link" href={href} key={label} target="_blank" rel="noreferrer">
                <Icon aria-hidden="true" size={18} />
                <span>{label}</span>
              </a>
            ))}
          </div>
        </div>

        <aside className="hero-evidence" aria-label="Portfolio evidence highlights">
          <div className="metric-block">
            <span>Selected impact</span>
            <strong>20.7K</strong>
            <p>Champions Voice followers gained in roughly 2-3 months through an AI-assisted weekly content loop.</p>
          </div>
          <div className="mini-grid">
            <span>350-400 emails</span>
            <span>2,374 rows cleaned</span>
            <span>8 AM brief</span>
            <span>0 theme errors</span>
          </div>
        </aside>
      </section>

      <section id="fit" className="section-block">
        <div className="section-heading">
          <p className="eyebrow">Why this maps to Claude Corps</p>
          <h2>Utility player evidence, organized around the role.</h2>
        </div>
        <div className="fit-grid">
          {fitSignals.map(({ title, text, icon: Icon }) => (
            <article className="fit-card" key={title}>
              <Icon aria-hidden="true" size={22} />
              <h3>{title}</h3>
              <p>{text}</p>
            </article>
          ))}
        </div>
      </section>

      <section id="case-studies" className="section-block case-section">
        <div className="section-heading split">
          <div>
            <p className="eyebrow">Selected systems</p>
            <h2>Five proof points from real workflows.</h2>
          </div>
          <p className="section-note">
            Screenshots are privacy-safe captures or reconstructions. Private emails,
            client records, and training details are intentionally redacted.
          </p>
        </div>

        <div className="case-list">
          {caseStudies.map((item, index) => (
            <article className="case-card" key={item.id}>
              <div className="case-media">
                <img src={asset(item.image)} alt={item.alt} loading="eager" />
              </div>
              <div className="case-content">
                <div className="case-title-row">
                  <item.icon aria-hidden="true" size={22} />
                  <div>
                    <p className="eyebrow">{item.eyebrow}</p>
                    <h3>{item.title}</h3>
                  </div>
                </div>
                <p className="case-summary">{item.summary}</p>
                <div className="stack-list" aria-label={`${item.title} stack`}>
                  {item.stack.map((tech) => (
                    <span key={tech}>{tech}</span>
                  ))}
                </div>
                <dl className="case-details">
                  <div>
                    <dt>Metric</dt>
                    <dd>{item.metric}</dd>
                  </div>
                  <div>
                    <dt>Problem</dt>
                    <dd>{item.problem}</dd>
                  </div>
                  <div>
                    <dt>Shipped</dt>
                    <dd>
                      <ul>
                        {item.shipped.map((line) => (
                          <li key={line}>{line}</li>
                        ))}
                      </ul>
                    </dd>
                  </div>
                  <div>
                    <dt>Handoff</dt>
                    <dd>{item.handoff}</dd>
                  </div>
                  <div>
                    <dt>Claude Corps signal</dt>
                    <dd>{item.signal}</dd>
                  </div>
                </dl>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section id="handoff" className="section-block handoff-section">
        <div className="section-heading">
          <p className="eyebrow">Operating style</p>
          <h2>Built for messy organizations and real owners.</h2>
        </div>
        <div className="principle-grid">
          {operatingPrinciples.map(({ title, text, icon: Icon }) => (
            <article className="principle-card" key={title}>
              <Icon aria-hidden="true" size={22} />
              <h3>{title}</h3>
              <p>{text}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section-block proof-band" aria-label="Certification and availability">
        <div>
          <CheckCircle2 aria-hidden="true" size={24} />
          <strong>Anthropic AI Fluency and Claude 101 certificates completed.</strong>
          <span>Proof available for application submission.</span>
        </div>
        <div>
          <Map aria-hidden="true" size={24} />
          <strong>U.S. work authorized and open to U.S. relocation.</strong>
          <span>Ready for an in-person host placement.</span>
        </div>
        <div>
          <LockKeyhole aria-hidden="true" size={24} />
          <strong>Privacy-aware portfolio evidence.</strong>
          <span>No private client emails, training data, or Notion records are published.</span>
        </div>
      </section>

      <footer className="site-footer">
        <div>
          <strong>Jakobi Davis</strong>
          <span>Brookhaven, GA | jakobi.davis@championsvoice.org</span>
        </div>
        <div className="footer-links">
          <a href="https://github.com/webdevkobi/claude-corps-ai-portfolio" target="_blank" rel="noreferrer">
            <Github aria-hidden="true" size={18} />
            <span>Repository</span>
          </a>
          <a href={`${import.meta.env.BASE_URL}resume/jakobi-davis-claude-corps-resume.pdf`} target="_blank" rel="noreferrer">
            <ClipboardList aria-hidden="true" size={18} />
            <span>Resume</span>
          </a>
          <a href="#top">
            <ShieldCheck aria-hidden="true" size={18} />
            <span>Top</span>
          </a>
        </div>
      </footer>
    </main>
  );
}

export default App;
