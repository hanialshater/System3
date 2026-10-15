// Names for the press's people (pure data). The founder may rename anyone: change the name here
// and run `node press/org/generate.mjs`. Names are chosen not to collide with System 3 Company's
// (its tools/org/people.mjs), because both orgs are shown in the same HQ.

export const PERSONA = {
  founder: "Hani",
  "vp-books": "Maren",
  "head-of-book-system-3": "Theodora",
  "writer-system-3": "Callum",
  "development-editor-system-3": "Harriet",
  "copy-editor-system-3": "Agnes",
  "fact-checker-system-3": "Beckett",
  "marketing-strategist-system-3": "Soledad",
  "experiment-developer-system-3": "Ilya",
  "swe-system-3-a": "Kasimir",
  "swe-system-3-b": "Noa",
  "art-director": "Ottavio",
  "release-manager-press": "Ruth",
  "review-arc": "Augustin",
  "review-easter-eggs": "Clementine",
  "review-narrative-momentum": "Dashiell",
  "review-llm-tells": "Vesna",
  "review-prose-quality": "Edith",
  "review-fun": "Jasper",
  "review-ideas": "Sunniva",
  "review-comparison": "Laurent",
};

export const nameFor = (id) => PERSONA[id] ?? id;
