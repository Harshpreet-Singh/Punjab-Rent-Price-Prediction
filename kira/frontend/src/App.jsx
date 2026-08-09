import RentForm from "./components/RentForm";
import useReveal from "./hooks/useReveal";

function App() {
  const howItWorksRef = useReveal();
  const estimatorRef = useReveal();
  const resultRef = useReveal();

  const scrollTo = (id) => {
    document.getElementById(id)?.scrollIntoView({
      behavior: "smooth",
    });
  };

  return (
    <main className="min-h-screen bg-white text-black">
      {/* Navbar */}
      <nav className="mx-auto flex max-w-7xl items-center justify-between px-6 py-6 lg:px-10">
        <button
          onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
          className="text-2xl font-black tracking-[-0.05em] transition-transform duration-300 hover:scale-105"
        >
          KIRA.
        </button>

        <button
          onClick={() => scrollTo("how-it-works")}
          className="group hidden items-center gap-2 rounded-full border border-black/10 bg-white px-5 py-3 text-sm font-semibold transition-all duration-300 hover:-translate-y-0.5 hover:border-kira-violet hover:text-kira-violet hover:shadow-md sm:flex"
        >
          How it works

          <span className="material-symbols-outlined text-[18px] transition-transform duration-300 group-hover:translate-x-1">
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

          <button
            onClick={() => scrollTo("estimator")}
            className="group mt-10 inline-flex items-center gap-3 rounded-full bg-kira-violet px-7 py-4 text-base font-bold text-white shadow-lg shadow-kira-violet/20 transition-all duration-300 ease-out hover:-translate-y-1 hover:bg-kira-violet-dark hover:shadow-xl hover:shadow-kira-violet/30 active:translate-y-0"
          >
            Estimate my rent

            <span className="material-symbols-outlined transition-transform duration-300 group-hover:translate-x-1">
              arrow_forward
            </span>
          </button>
        </div>

        {/* Scroll indicator */}
        <button
          onClick={() => scrollTo("how-it-works")}
          className="group mt-20 flex w-fit items-center gap-3 text-sm font-semibold text-kira-muted"
        >
          <span className="material-symbols-outlined text-[20px] transition-transform duration-300 group-hover:translate-y-1">
            south
          </span>

          <span className="transition-colors duration-300 group-hover:text-kira-violet">
            Scroll to explore
          </span>
        </button>
      </section>

      {/* How KIRA Works */}
      <section
        id="how-it-works"
        ref={howItWorksRef}
        className="reveal bg-kira-dark px-6 py-28 text-white lg:px-10"
      >
        <div className="mx-auto max-w-7xl">
          <p className="text-sm font-bold uppercase tracking-[0.25em] text-kira-violet-light">
            How KIRA works
          </p>

          <h2 className="mt-6 max-w-4xl text-5xl font-extrabold leading-tight tracking-[-0.04em] sm:text-6xl lg:text-8xl">
            Tell us about
            <br />
            your next place.
          </h2>

          <div className="mt-20 grid gap-6 md:grid-cols-3">
            {/* Card 1 */}
            <div className="group rounded-3xl border border-white/10 bg-white/5 p-8 transition-all duration-300 ease-out hover:-translate-y-2 hover:border-kira-violet/40 hover:bg-white/[0.07] hover:shadow-2xl hover:shadow-black/20">
              <span className="material-symbols-outlined text-4xl text-kira-violet-light transition-transform duration-300 group-hover:-rotate-3 group-hover:scale-110">
                edit_location_alt
              </span>

              <p className="mt-8 text-sm font-bold uppercase tracking-widest text-white/50">
                01
              </p>

              <h3 className="mt-3 text-2xl font-bold">
                Choose your location
              </h3>

              <p className="mt-4 leading-7 text-white/60">
                Select your city and area instead of typing complicated
                location details.
              </p>
            </div>

            {/* Card 2 */}
            <div className="group rounded-3xl border border-white/10 bg-white/5 p-8 transition-all duration-300 ease-out hover:-translate-y-2 hover:border-kira-violet/40 hover:bg-white/[0.07] hover:shadow-2xl hover:shadow-black/20">
              <span className="material-symbols-outlined text-4xl text-kira-violet-light transition-transform duration-300 group-hover:-rotate-3 group-hover:scale-110">
                home
              </span>

              <p className="mt-8 text-sm font-bold uppercase tracking-widest text-white/50">
                02
              </p>

              <h3 className="mt-3 text-2xl font-bold">
                Describe the property
              </h3>

              <p className="mt-4 leading-7 text-white/60">
                Add bedrooms, bathrooms, area, furnishing and property type.
              </p>
            </div>

            {/* Card 3 */}
            <div className="group rounded-3xl border border-white/10 bg-white/5 p-8 transition-all duration-300 ease-out hover:-translate-y-2 hover:border-kira-violet/40 hover:bg-white/[0.07] hover:shadow-2xl hover:shadow-black/20">
              <span className="material-symbols-outlined text-4xl text-kira-violet-light transition-transform duration-300 group-hover:-rotate-3 group-hover:scale-110">
                auto_awesome
              </span>

              <p className="mt-8 text-sm font-bold uppercase tracking-widest text-white/50">
                03
              </p>

              <h3 className="mt-3 text-2xl font-bold">
                Get your estimate
              </h3>

              <p className="mt-4 leading-7 text-white/60">
                KIRA uses our trained rental model to estimate the monthly
                rent.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Estimator */}
      <section
        id="estimator"
        ref={estimatorRef}
        className="reveal bg-kira-light px-6 py-28 lg:px-10"
      >
        <div className="mx-auto max-w-7xl">
          <div className="max-w-3xl">
            <p className="text-sm font-bold uppercase tracking-[0.25em] text-kira-violet">
              Estimate your rent
            </p>

            <h2 className="mt-6 text-5xl font-extrabold leading-tight tracking-[-0.04em] sm:text-6xl lg:text-8xl">
              Find the number
              <br />
              before you move.
            </h2>

            <p className="mt-6 max-w-xl text-lg leading-8 text-kira-muted">
              Tell KIRA about the property you're considering and get a
              data-driven monthly rent estimate.
            </p>
          </div>

          <div className="mt-16">
            <RentForm />
          </div>
        </div>
      </section>

      {/* Prediction Result */}
      <section
        ref={resultRef}
        className="reveal bg-kira-dark px-6 py-28 text-white lg:px-10"
      >
        <div className="mx-auto max-w-7xl">
          <p className="text-sm font-bold uppercase tracking-[0.25em] text-kira-violet-light">
            Your estimate
          </p>

          <div className="mt-10 rounded-[2rem] border border-white/10 bg-white/5 p-8 transition-all duration-500 hover:border-kira-violet/30 hover:bg-white/[0.07] sm:p-12">
            <div className="flex flex-col justify-between gap-10 sm:flex-row sm:items-end">
              <div>
                <p className="text-sm font-semibold text-white/50">
                  Estimated monthly rent
                </p>

                <p className="mt-3 text-6xl font-extrabold tracking-tight transition-transform duration-500 sm:text-8xl">
                  ₹ —
                </p>
              </div>

              <div className="max-w-sm">
                <p className="text-sm leading-6 text-white/50">
                  Your prediction will appear here after you submit the
                  property details.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-black px-6 py-10 text-white lg:px-10">
        <div className="mx-auto flex max-w-7xl flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
          <p className="text-lg font-black tracking-[-0.04em]">
            KIRA.
          </p>

          <p className="text-sm text-white/40">
            Punjab Rent Intelligence
          </p>
        </div>
      </footer>
    </main>
  );
}

export default App;