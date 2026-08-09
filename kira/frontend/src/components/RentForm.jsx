import { useState } from "react";

function RentForm() {
  const [formData, setFormData] = useState({
    bhk: 2,
    bathroom: 2,
    area: "",
    city: "",
    location: "",
    furnishing: "",
    propertyType: "",
  });

  const updateField = (field, value) => {
    setFormData((current) => ({
      ...current,
      [field]: value,
    }));
  };

  const inputClasses = `
    mt-3 w-full rounded-xl
    border border-black/10
    bg-white px-4 py-3
    outline-none
    transition-all duration-200
    hover:border-black/20
    focus:border-kira-violet
    focus:ring-4
    focus:ring-kira-violet/10
  `;

  const selectClasses = `
    mt-3 w-full rounded-xl
    border border-black/10
    bg-white px-4 py-3
    outline-none
    transition-all duration-200
    hover:border-black/20
    focus:border-kira-violet
    focus:ring-4
    focus:ring-kira-violet/10
  `;

  const counterButtonClasses = `
    flex h-12 w-12 items-center justify-center
    rounded-xl border border-black/10
    transition-all duration-200
    hover:-translate-y-0.5
    hover:border-kira-violet
    hover:bg-kira-violet/5
    hover:text-kira-violet
    active:scale-95
  `;

  return (
    <div className="rounded-[2rem] border border-black/10 bg-white p-6 shadow-xl shadow-black/5 transition-shadow duration-500 hover:shadow-2xl hover:shadow-black/10 sm:p-8 lg:p-10">
      {/* Header */}
      <div className="mb-10">
        <p className="text-sm font-bold uppercase tracking-[0.2em] text-kira-violet">
          Property details
        </p>

        <h3 className="mt-3 text-3xl font-extrabold tracking-tight sm:text-4xl">
          Tell us what you're looking for.
        </h3>

        <p className="mt-3 max-w-xl leading-7 text-kira-muted">
          A few details are all KIRA needs to estimate your monthly rent.
        </p>
      </div>

      {/* Bedrooms */}
      <div>
        <label className="text-sm font-bold">
          Bedrooms
        </label>

        <div className="mt-3 flex items-center gap-3">
          <button
            type="button"
            onClick={() =>
              updateField(
                "bhk",
                Math.max(1, formData.bhk - 1)
              )
            }
            className={counterButtonClasses}
          >
            <span className="material-symbols-outlined">
              remove
            </span>
          </button>

          <div className="flex h-12 min-w-20 items-center justify-center rounded-xl bg-kira-light text-lg font-bold">
            {formData.bhk} BHK
          </div>

          <button
            type="button"
            onClick={() =>
              updateField(
                "bhk",
                Math.min(10, formData.bhk + 1)
              )
            }
            className={counterButtonClasses}
          >
            <span className="material-symbols-outlined">
              add
            </span>
          </button>
        </div>
      </div>

      {/* Bathroom + Area */}
      <div className="mt-8 grid gap-6 sm:grid-cols-2">
        <div>
          <label className="text-sm font-bold">
            Bathrooms
          </label>

          <input
            type="number"
            min="1"
            value={formData.bathroom}
            onChange={(event) =>
              updateField("bathroom", event.target.value)
            }
            className={inputClasses}
            placeholder="2"
          />
        </div>

        <div>
          <label className="text-sm font-bold">
            Area
          </label>

          <div className="relative">
            <input
              type="number"
              min="1"
              value={formData.area}
              onChange={(event) =>
                updateField("area", event.target.value)
              }
              className={`${inputClasses} pr-20`}
              placeholder="1200"
            />

            <span className="pointer-events-none absolute right-4 top-1/2 mt-1 -translate-y-1/2 text-sm font-semibold text-kira-muted">
              sqft
            </span>
          </div>
        </div>
      </div>

      {/* City + Location */}
      <div className="mt-8 grid gap-6 sm:grid-cols-2">
        <div>
          <label className="text-sm font-bold">
            City
          </label>

          <select
            value={formData.city}
            onChange={(event) =>
              updateField("city", event.target.value)
            }
            className={selectClasses}
          >
            <option value="">
              Select city
            </option>
            <option>SAS Nagar</option>
            <option>Kharar</option>
            <option>Mohali</option>
          </select>
        </div>

        <div>
          <label className="text-sm font-bold">
            Location
          </label>

          <select
            value={formData.location}
            onChange={(event) =>
              updateField("location", event.target.value)
            }
            className={selectClasses}
          >
            <option value="">
              Select location
            </option>
            <option>Phase 7</option>
            <option>Phase 3B2</option>
            <option>Sector 70</option>
          </select>
        </div>
      </div>

      {/* Furnishing + Property Type */}
      <div className="mt-8 grid gap-6 sm:grid-cols-2">
        <div>
          <label className="text-sm font-bold">
            Furnishing
          </label>

          <select
            value={formData.furnishing}
            onChange={(event) =>
              updateField("furnishing", event.target.value)
            }
            className={selectClasses}
          >
            <option value="">
              Select furnishing
            </option>
            <option>Fully Furnished</option>
            <option>Semi Furnished</option>
            <option>Furnished</option>
            <option>Unknown</option>
          </select>
        </div>

        <div>
          <label className="text-sm font-bold">
            Property type
          </label>

          <select
            value={formData.propertyType}
            onChange={(event) =>
              updateField("propertyType", event.target.value)
            }
            className={selectClasses}
          >
            <option value="">
              Select type
            </option>
            <option>Apartment</option>
            <option>Flat</option>
            <option>Independent House</option>
            <option>Independent Floor</option>
            <option>Room Set</option>
            <option>PG</option>
          </select>
        </div>
      </div>

      {/* Submit */}
      <button
        type="button"
        className="
          group mt-10 flex w-full
          items-center justify-center gap-3
          rounded-2xl
          bg-kira-violet
          px-6 py-4
          font-bold text-white
          shadow-lg shadow-kira-violet/20
          transition-all duration-300 ease-out
          hover:-translate-y-1
          hover:bg-kira-violet-dark
          hover:shadow-xl
          hover:shadow-kira-violet/30
          active:translate-y-0
          active:scale-[0.99]
        "
      >
        Predict my rent

        <span className="material-symbols-outlined transition-transform duration-300 group-hover:translate-x-1">
          arrow_forward
        </span>
      </button>
    </div>
  );
}

export default RentForm;