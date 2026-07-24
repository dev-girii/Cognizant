# Hands-on 10: API Integration & Advanced State Management

This repository contains the advanced implementation for consolidating our API layer and managing academic course state securely and robustly using React & Redux Toolkit.

---

## 📊 Framework State Management Comparison

Below is a detailed comparison comparing **React + Redux Toolkit (RTK)**, **Angular + NgRx**, and **Vue + Pinia** across key technical dimensions:

| Dimension | React + Redux Toolkit (RTK) | Angular + NgRx | Vue + Pinia |
| :--- | :--- | :--- | :--- |
| **Architectural Pattern** | Redux flow (Action → Reducer → Selector → Store). Multi-slice architecture with Async Thunks for side effects. | RxJS-powered Redux flow (Action → Reducer → Selector → Effects). Unidirectional reactive streams. | Decentralized store architecture. Actions combine both synchronous mutations and asynchronous calls. |
| **Boilerplate Requirements** | **Moderate**. RTK (`createSlice`, `createAsyncThunk`) eliminates classic Redux boilerplate, but still requires actions, extraReducers, and selectors. | **High**. Requires distinct action declarations, reducers, selectors, service injections, and RxJS-driven side-effect classes (Effects). | **Very Low**. No mutations or separate thunks needed; state is mutated directly, and async actions are simple methods. |
| **Learning Curve** | **Moderate**. Requires understanding unidirectional data flow, immutable state updates (handled by Immer under the hood), and thunk lifecycles. | **Steep**. Demands a deep mastery of RxJS operators (`switchMap`, `mergeMap`, etc.) and observable-driven state streams. | **Low**. Extremely intuitive composition API design that feels similar to regular Vue reactive refs. |
| **Built-in Tooling & DevExperience** | Excellent. Fully integrates with Redux DevTools for time-travel debugging, state diffs, and action tracing. | Excellent. Direct integration with Redux DevTools plus Angular CLI commands for generating actions/reducers. | Excellent. Directly supported in the Vue DevTools extension, including state inspections, actions tracking, and time-travel. |
| **Reactive Paradigm** | Virtual DOM updates via subscription selector hooks (`useSelector`). | RxJS Streams & Async Pipe in templates (fully push-based). | Vue Reactivity System (Proxy-based properties and `storeToRefs`). |

---

### Key Takeaways

1. **Redux Toolkit** is perfect for React developers seeking a predictable, globally structured store with robust developer tooling, without the massive verbosity of vanilla Redux.
2. **NgRx** is highly beneficial in enterprise-scale Angular applications that rely heavily on complex, asynchronous event flows and utilize RxJS streams throughout the codebase.
3. **Pinia** represents the modern wave of state management, stripping away unnecessary structural layers while maintaining strong TypeScript integration and excellent reactivity mechanics.
