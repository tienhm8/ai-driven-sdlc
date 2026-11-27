---
name: react
description: "Write or review React component logic: state ownership, derived state, effects, keys, composition, focus, and keyboard behavior. Baseline React 19.2.3 as used by base-web. Use alongside umi-max when a change affects component behavior."
metadata:
  react-version: "19.2.3"
---

# React 19.2.3

Use this when a change affects how a component behaves, not for routing, models, or API wiring (see the `umi-max` skill for those).

1. Read the task, the nearest working component, and the React version in the lockfile. Follow existing conventions before introducing a pattern.
2. Keep state next to where it is used and lift it only when two components need it. Compute derived values during render instead of storing them in state.
3. Use an effect only to synchronize with something outside React (network, timers, subscriptions, the DOM). Do not use an effect to compute data or to respond to an event that a handler can handle. Clean up what an effect starts, and make sure a slower, older response cannot overwrite a newer one.
4. Give list items stable keys from the record, not the array index, when items can reorder, insert, or delete.
5. Prefer composition over prop drilling and over duplicated near-identical components. Pass only the props a child needs.
6. Keep interactive elements keyboard-operable with visible focus and accessible names; an icon-only control needs a label. Manage focus when opening and closing modals or drawers.
7. Optimize rendering only with evidence of a problem; avoid speculative memoization.
8. Test the behavior: user interaction, empty and error states, and keyboard use. Report what you exercised and what you could not verify.

When the change also touches routes, models, requests, or tables in `base-web`, load `umi-max` rather than repeating its guidance here.
