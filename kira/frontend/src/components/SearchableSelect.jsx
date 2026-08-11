import { useEffect, useRef, useState } from "react";

function SearchableSelect({
  value,
  onChange,
  options = [],
  placeholder = "Search...",
  disabled = false,
  error = "",
}) {
  const [isOpen, setIsOpen] = useState(false);
  const [search, setSearch] = useState("");

  const containerRef = useRef(null);
  const inputRef = useRef(null);

  const filteredOptions = options.filter((option) =>
    option.toLowerCase().includes(search.toLowerCase()),
  );

  useEffect(() => {
    const handleOutsideClick = (event) => {
      if (
        containerRef.current &&
        !containerRef.current.contains(event.target)
      ) {
        setIsOpen(false);
      }
    };

    document.addEventListener("mousedown", handleOutsideClick);

    return () => {
      document.removeEventListener("mousedown", handleOutsideClick);
    };
  }, []);

  useEffect(() => {
    if (!value) {
      setSearch("");
    }
  }, [value]);

  const handleSelect = (option) => {
    onChange(option);
    setSearch("");
    setIsOpen(false);
  };

  const handleOpen = () => {
    if (disabled) return;

    setIsOpen(true);

    setTimeout(() => {
      inputRef.current?.focus();
    }, 0);
  };

  return (
    <div ref={containerRef} className="relative">
      <button
        type="button"
        onClick={handleOpen}
        disabled={disabled}
        className={`
          ${value ? "text-black" : "text-kira-muted"}
          ${error ? "border-red-400" : "border-black/10"}
          mt-3 flex w-full items-center justify-between
          rounded-xl border
          bg-white px-4 py-3
          text-left
          outline-none
          transition-all duration-200
          hover:border-black/20
          focus:border-kira-violet
          focus:ring-4
          focus:ring-kira-violet/10
          disabled:cursor-not-allowed
          disabled:bg-black/3
        `}
      >
        <span className="truncate">
          {value || placeholder}
        </span>

        <span
          className={`
            material-symbols-outlined
            text-[20px]
            transition-transform duration-200
            ${isOpen ? "rotate-180" : ""}
          `}
        >
          expand_more
        </span>
      </button>

      {isOpen && (
        <div className="absolute z-50 mt-2 w-full overflow-hidden rounded-xl border border-black/10 bg-white shadow-xl">
          {/* Search */}
          <div className="border-b border-black/10 p-2">
            <div className="relative">
              <span className="material-symbols-outlined pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-[20px] text-kira-muted">
                search
              </span>

              <input
                ref={inputRef}
                type="text"
                value={search}
                onChange={(event) => setSearch(event.target.value)}
                placeholder={placeholder}
                className="
                  w-full rounded-lg
                  bg-kira-light
                  py-2.5 pl-10 pr-3
                  text-sm
                  outline-none
                  transition-all duration-200
                  focus:ring-2
                  focus:ring-kira-violet/10
                "
              />
            </div>
          </div>

          {/* Options */}
          <div className="max-h-60 overflow-y-auto p-1">
            {filteredOptions.length > 0 ? (
              filteredOptions.map((option) => (
                <button
                  key={option}
                  type="button"
                  onClick={() => handleSelect(option)}
                  className={`
                    flex w-full items-center justify-between
                    rounded-lg px-3 py-2.5
                    text-left text-sm
                    transition-colors duration-150
                    hover:bg-kira-violet/5
                    hover:text-kira-violet
                    ${
                      value === option
                        ? "bg-kira-violet/10 font-semibold text-kira-violet"
                        : ""
                    }
                  `}
                >
                  <span>{option}</span>

                  {value === option && (
                    <span className="material-symbols-outlined text-[18px]">
                      check
                    </span>
                  )}
                </button>
              ))
            ) : (
              <div className="px-3 py-8 text-center text-sm text-kira-muted">
                No locations found.
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default SearchableSelect;