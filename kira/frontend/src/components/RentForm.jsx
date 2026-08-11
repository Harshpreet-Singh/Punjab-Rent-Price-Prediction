import { useState } from "react";
import { useForm } from "react-hook-form";

function RentForm({ onPrediction }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const {
    register,
    handleSubmit,
    setValue,
    watch,
    formState: { errors },
  } = useForm({
    defaultValues: {
      bhk: 2,
      bathroom: 2,
      area: "",
      city: "",
      location: "",
      furnishing: "",
      propertyType: "",
    },
  });

  const bhk = watch("bhk");
  // const [loading, setLoading] = useState(false);
  // const [error, setError] = useState("");

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

  const onSubmit = async (formData) => {
    setError("");
    setLoading(true);

    try {
      const payload = {
        bhk: Number(formData.bhk),
        bathroom: Number(formData.bathroom),
        area: Number(formData.area),
        city: formData.city,
        location: formData.location,
        furnishing: formData.furnishing,
        property_type: formData.propertyType,
      };

      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Unable to predict rent. Please try again.",
        );
      }

      onPrediction(data.predicted_rent);
    } catch (err) {
      console.error("Prediction error:", err);
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* Header */}
      <div>
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
      <div className="mt-8">
        <label className="text-sm font-bold">Bedrooms</label>

        <div className="mt-3 flex items-center gap-3">
          <button
            type="button"
            onClick={() => setValue("bhk", Math.max(1, bhk - 1))}
            className={counterButtonClasses}
          >
            <span className="material-symbols-outlined">remove</span>
          </button>

          <div className="flex h-12 min-w-20 items-center justify-center rounded-xl bg-kira-light text-lg font-bold">
            {bhk} BHK
          </div>

          <button
            type="button"
            onClick={() => setValue("bhk", Math.min(10, bhk + 1))}
            className={counterButtonClasses}
          >
            <span className="material-symbols-outlined">add</span>
          </button>
        </div>
      </div>

      {/* Bathroom + Area */}
      <div className="mt-8 grid gap-6 sm:grid-cols-2">
        <div>
          <label className="text-sm font-bold">Bathrooms</label>
          <input
            type="number"
            min="1"
            max="10"
            {...register("bathroom", {
              required: "Please enter the number of bathrooms.",
              min: {
                value: 1,
                message: "Bathrooms must be at least 1.",
              },
              max: {
                value: 10,
                message: "Bathrooms cannot exceed 10.",
              },
              valueAsNumber: true,
            })}
            className={inputClasses}
            placeholder="2"
          />

          {errors.bathroom && (
            <p className="mt-2 text-sm font-medium text-red-500">
              {errors.bathroom.message}
            </p>
          )}
        </div>

        <div>
          <label className="text-sm font-bold">Area</label>

          <div className="relative">
            <input
              type="number"
              min="1"
              max="10000"
              {...register("area", {
                required: "Please enter the property area.",
                min: {
                  value: 1,
                  message: "Area must be at least 1 sqft.",
                },
                max: {
                  value: 10000,
                  message: "Area cannot exceed 10,000 sqft.",
                },
                valueAsNumber: true,
              })}
              className={`${inputClasses} pr-20`}
              placeholder="1200"
            />

            <span className="pointer-events-none absolute right-4 top-1/2 mt-1 -translate-y-1/2 text-sm font-semibold text-kira-muted">
              sqft
            </span>
            {errors.area && (
              <p className="mt-2 text-sm font-medium text-red-500">
                {errors.area.message}
              </p>
            )}
          </div>
        </div>
      </div>

      {/* City + Location */}
      <div className="mt-8 grid gap-6 sm:grid-cols-2">
        <div>
          <label className="text-sm font-bold">City</label>

          <select
            {...register("city", {
              required: "Please select a city.",
            })}
            className={selectClasses}
          >
            <option value="">Select city</option>
            <option>SAS Nagar</option>
            <option>Kharar</option>
            <option>Mohali</option>
          </select>

          {errors.city && (
            <p className="mt-2 text-sm font-medium text-red-500">
              {errors.city.message}
            </p>
          )}
        </div>

        <div>
          <label className="text-sm font-bold">Location</label>

          <select
            {...register("location", {
              required: "Please select a location.",
            })}
            className={selectClasses}
          >
            <option value="">Select location</option>
            <option>Phase 7</option>
            <option>Phase 3B2</option>
            <option>Sector 70</option>
          </select>

          {errors.location && (
            <p className="mt-2 text-sm font-medium text-red-500">
              {errors.location.message}
            </p>
          )}
        </div>
      </div>

      {/* Furnishing + Property Type */}
      <div className="mt-8 grid gap-6 sm:grid-cols-2">
        <div>
          <label className="text-sm font-bold">Furnishing</label>

          <select
            {...register("furnishing", {
              required: "Please select the furnishing type.",
            })}
            className={selectClasses}
          >
            <option value="">Select furnishing</option>
            <option>Fully Furnished</option>
            <option>Semi Furnished</option>
            <option>Furnished</option>
            <option>Unknown</option>
          </select>

          {errors.furnishing && (
            <p className="mt-2 text-sm font-medium text-red-500">
              {errors.furnishing.message}
            </p>
          )}
        </div>

        <div>
          <label className="text-sm font-bold">Property type</label>

          <select
            {...register("propertyType", {
              required: "Please select the property type.",
            })}
            className={selectClasses}
          >
            <option value="">Select type</option>
            <option>Apartment</option>
            <option>Flat</option>
            <option>Independent House</option>
            <option>Independent Floor</option>
            <option>Room Set</option>
            <option>PG</option>
          </select>

          {errors.propertyType && (
            <p className="mt-2 text-sm font-medium text-red-500">
              {errors.propertyType.message}
            </p>
          )}
        </div>
      </div>

      {/* Submit */}
      <button
        type="submit"
        disabled={loading}
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
          disabled:cursor-not-allowed
          disabled:opacity-60
          disabled:hover:translate-y-0
        "
      >
        {loading ? "Estimating..." : "Predict my rent"}

        {!loading && (
          <span className="material-symbols-outlined transition-transform duration-300 group-hover:translate-x-1">
            arrow_forward
          </span>
        )}
      </button>
    </form>
  );
}

export default RentForm;
