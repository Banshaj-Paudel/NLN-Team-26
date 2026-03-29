import Button from '../ui/Button'
import SectionHeader from '../ui/SectionHeader'
import AnchorCard from '../components/AnchorCard'
import ChallengeItem from '../components/ChallengeItem'
import FeatureCard from '../components/FeatureCard'
import ForecastCard from '../components/ForecastCard'
import HeatmapCard from '../components/HeatmapCard'
import StatCard from '../components/StatCard'

const stats = [
  {
    value: '55%',
    label: 'College students report academic burnout',
    source: 'Crown Counseling',
  },
  {
    value: '70%',
    label: 'Gen Z & Millennials felt burnout in the last year',
    source: 'The Interview Guys',
  },
  {
    value: '80%',
    label: 'Graduating seniors worry about future burnout',
    source: 'Higher Ed Dive',
  },
  {
    value: '37%',
    label: 'Screen positive for moderate-to-severe depression',
    source: 'High 5 Test',
  },
  {
    value: '82%',
    label: 'White-collar workers globally feel burned out',
    source: 'HR Brew',
  },
  {
    value: '$125B+',
    label: 'Annual healthcare cost of burnout in the U.S.',
    source: 'Spill',
  },
]

const features = [
  {
    title: 'Burnout Forecast Card',
    copy: 'A weekly stress weather report that spots risk 3-6 weeks early with a calm, human tone.',
    tag: 'Forecast',
  },
  {
    title: 'Anchor Matching',
    copy: 'Pairs users with a verified peer who has lived the same pressure - not a chatbot.',
    tag: 'Mentorship',
  },
  {
    title: 'Pressure Maps',
    copy: 'Anonymous community heatmaps show which stages feel the most intense right now.',
    tag: 'Community',
  },
  {
    title: 'Micro-Recovery Challenges',
    copy: 'Contextual 5-minute resets based on deadlines, sleep, and workload patterns.',
    tag: 'Recovery',
  },
  {
    title: 'Career Clarity Sessions',
    copy: 'Structured 30-minute conversations about uncertainty, not therapy.',
    tag: 'Clarity',
  },
  {
    title: 'Burnout Passport',
    copy: 'A private log of stress signals, coping wins, and milestones - exportable and owned by the user.',
    tag: 'Ownership',
  },
]

const signals = [
  'Sleep patterns',
  'Workload logs',
  'Mood check-ins',
  'Task completion rate',
  'Deadline proximity',
  'Career-stage context',
]

const challenges = [
  {
    title: '5-minute reset',
    detail: 'You skipped lunch twice. Try a short stretch + hydration timer.',
  },
  {
    title: 'Deadline decompression',
    detail: 'Due in 3 days? Use a 15-minute plan + a single next action.',
  },
  {
    title: 'Energy refill',
    detail: 'Low sleep streak? Swap one task for a focused 25-minute sprint.',
  },
]

function BurnMapLanding() {
  return (
    <div className="burnmap">
      <header className="topbar">
        <div className="logo">
          <span className="logo-mark"></span>
          <span>BurnMap</span>
        </div>
        <nav className="nav">
          <a href="#solution">Solution</a>
          <a href="#features">Features</a>
          <a href="#maps">Pressure Maps</a>
          <a href="#passport">Passport</a>
        </nav>
        <Button variant="ghost">Join the waitlist</Button>
      </header>

      <main>
        <section className="hero" id="solution">
          <div className="hero-copy">
            <p className="eyebrow">Proactive burnout forecasting + peer mentorship</p>
            <h1>
              Predict burnout before it breaks momentum - and match people to humans who made it through.
            </h1>
            <p className="lead">
              BurnMap watches the quiet signals of overload, forecasts risk early, and connects students and
              early-career professionals to Anchors who have lived the same pressure.
            </p>
            <div className="cta-row">
              <Button variant="primary">Start a forecast</Button>
              <Button variant="secondary">Meet the Anchors</Button>
            </div>
            <div className="signal-grid">
              {signals.map((signal) => (
                <span key={signal} className="signal-chip">
                  {signal}
                </span>
              ))}
            </div>
          </div>

          <div className="hero-visual">
            <ForecastCard
              status="Amber"
              riskValue="62%"
              riskLabel="Rising risk in 3-4 weeks"
              note="Skipped lunch twice, 3 deadlines ahead, sleep down 18%"
            />
            <AnchorCard
              role="Senior CS grad - job search survivor"
              name="Aanya P."
              quote="I went through the same interview spiral. Here's the reset plan that helped me."
            />
          </div>
        </section>

        <section className="stats" aria-label="Burnout statistics">
          <SectionHeader
            title="The scale is real - and rising"
            subtitle="Burnout is building long before people ask for help. BurnMap focuses on early signals so people do not disappear from their path."
          />
          <div className="stat-grid">
            {stats.map((stat) => (
              <StatCard key={stat.label} value={stat.value} label={stat.label} source={stat.source} />
            ))}
          </div>
        </section>

        <section className="story">
          <div className="story-panel">
            <h3>Burnout does not show up overnight.</h3>
            <p>
              It grows slowly: pressure piles up, career clarity fades, and financial anxiety amplifies every
              decision. BurnMap watches the build-up so intervention feels calm, not clinical.
            </p>
            <div className="timeline">
              <span>High academic pressure</span>
              <span>Unclear career paths</span>
              <span>Financial anxiety</span>
              <span>Burnout</span>
              <span>Mental health decline</span>
            </div>
          </div>
          <div className="story-panel highlight">
            <h3>Meet the Anchor effect.</h3>
            <p>
              Anchors are trained peers 2-3 years ahead. They have walked the same path and can talk about
              uncertainty without the stigma of "therapy."
            </p>
            <div className="anchor-stack">
              <div className="anchor-chip">Final-year med student</div>
              <div className="anchor-chip">Junior developer</div>
              <div className="anchor-chip">Career switcher</div>
            </div>
          </div>
        </section>

        <section className="features" id="features">
          <SectionHeader
            title="Features built for the moment before burnout"
            subtitle="Each module is designed to spot overload early, contextualize it to the career stage, and give a human path forward."
          />
          <div className="feature-grid">
            {features.map((feature) => (
              <FeatureCard
                key={feature.title}
                title={feature.title}
                copy={feature.copy}
                tag={feature.tag}
              />
            ))}
          </div>
        </section>

        <section className="maps" id="maps">
          <SectionHeader
            title="Pressure Maps show you are not alone"
            subtitle="Anonymous, crowd-sourced heatmaps reveal which semesters, job tracks, and milestones feel the heaviest right now."
          />
          <div className="maps-grid">
            <HeatmapCard
              title="Semester 7 - CS Track"
              subtitle="Highest stress zones this month"
              status="Red"
              tags={['Job rejections', 'Capstone', 'Visa anxiety']}
            />

            <div className="map-card list">
              <h3>Micro-recovery challenges</h3>
              <p>Short, contextual actions delivered when signals spike.</p>
              <div className="challenge-list">
                {challenges.map((challenge) => (
                  <ChallengeItem key={challenge.title} title={challenge.title} detail={challenge.detail} />
                ))}
              </div>
            </div>
          </div>
        </section>

        <section className="passport" id="passport">
          <div className="passport-card">
            <div>
              <p className="eyebrow">Burnout Passport</p>
              <h2>Your stress history, owned by you.</h2>
              <p>
                Export a private log of stress signals, coping tools, and milestones survived. Share it only
                when you choose - or keep it fully local.
              </p>
              <Button variant="secondary">Download sample passport</Button>
            </div>
            <div className="passport-preview">
              <div className="passport-line"></div>
              <div className="passport-line"></div>
              <div className="passport-line"></div>
              <div className="passport-milestone">
                <span>Milestone</span>
                <strong>Survived final exams week</strong>
              </div>
              <div className="passport-line"></div>
              <div className="passport-line"></div>
            </div>
          </div>
        </section>

        <section className="cta">
          <div className="cta-card">
            <h2>Let's stop burnout before it starts.</h2>
            <p>
              Join the waitlist for early access and help shape a platform that respects privacy and delivers
              real human support.
            </p>
            <div className="cta-row">
              <Button variant="primary">Request early access</Button>
              <Button variant="ghost">Talk to the team</Button>
            </div>
          </div>
        </section>
      </main>

      <footer className="footer">
        <div>
          <span className="logo-mark"></span>
          <strong>BurnMap</strong>
        </div>
        <p>All behavioral data stays local first and syncs only with explicit consent.</p>
      </footer>
    </div>
  )
}

export default BurnMapLanding
