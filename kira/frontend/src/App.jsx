function App() {
  return (
    <main className="min-h-screen bg-kira-surface text-kira-ink">
      {/* Navbar */}
      <nav className="mx-auto flex max-w-7xl items-center justify-between px-6 py-6 lg:px-10">
        <div className="text-2xl font-extrabold tracking-tight">
          KIRA<span className="text-kira-violet">.</span>
        </div>

        <button className="hidden items-center gap-2 rounded-full border border-black/10 bg-white px-5 py-3 text-sm font-semibold transition hover:border-kira-violet hover:text-kira-violet sm:flex">
          How it works
          <span className="material-symbols-outlined text-[18px]">
            arrow_forward
          </span>
        </button>
      </nav>

      {/* Hero */}
      <section className="mx-auto flex min-h-[calc(100vh-100px)] max-w-7xl flex-col justify-center px-6 pb-20 pt-12 lg:px-10">
        <div className="max-w-5xl">
          <p className="mb-6 text-sm font-bold uppercase tracking-[0.25em] text-kira-violet">
            Punjab rent intelligence
          </p>

          <h1 className="text-6xl font-extrabold leading-[0.95] tracking-[-0.05em] sm:text-7xl lg:text-9xl">
            Know your rent.
            <br />
            <span className="text-kira-violet">Before you move.</span>
          </h1>

          <p className="mt-8 max-w-xl text-lg leading-8 text-kira-muted sm:text-xl">
            Get a smart estimate for your next flat, apartment, house or PG —
            powered by real rental data from Punjab.
          </p>

          <button className="mt-10 inline-flex items-center gap-3 rounded-full bg-kira-violet px-7 py-4 text-base font-bold text-white shadow-lg shadow-kira-violet/20 transition duration-300 hover:-translate-y-1 hover:bg-kira-violet-dark">
            Estimate my rent

            <span className="material-symbols-outlined">
              arrow_forward
            </span>
          </button>
        </div>

        {/* Scroll indicator */}
        <div className="mt-20 flex items-center gap-3 text-sm font-semibold text-kira-muted">
          <span className="material-symbols-outlined text-[20px]">
            south
          </span>

          Scroll to explore
        </div>
      </section>

      {/* Dark section placeholder */}
      <section className="min-h-[60vh] bg-kira-dark px-6 py-24 text-white lg:px-10">
        <div className="mx-auto max-w-7xl">
          <p className="text-sm font-bold uppercase tracking-[0.25em] text-kira-violet-light">
            Your next move
          </p>

          <h2 className="mt-6 max-w-4xl text-5xl font-extrabold leading-tight tracking-[-0.04em] sm:text-6xl lg:text-8xl">
            Let's figure out
            <br />
            what it should cost.
          </h2>
        </div>
      </section>
    </main>
  )
}

export default App