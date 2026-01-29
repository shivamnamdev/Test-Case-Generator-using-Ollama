# SOP: Frontend UI (Web)

## 1. Goal
Provide a premium, glassmorphic chat interface for users to input code and receive test cases.

## 2. Structure
- **HTML**: Single page (`index.html`).
- **CSS**: Custom `styles.css` (Glassmorphism, dark mode, neon accents).
- **JS**: Vanilla `script.js` for API calls and DOM manipulation.

## 3. Logic Flow
1. **User Input**: User pastes code into a textarea.
2. **Submit**: User clicks "Generate Tests".
3. **Loading State**: Button shows spinner; UI locks.
4. **API Call**: `fetch('POST /generate', body)`.
5. **Render**:
    - **Success**: Display code in a syntax-highlighted block (using `Prism.js` or similar if available, or simple pre/code tags).
    - **Error**: Show toast notification with error message.

## 4. Aesthetics
- **Theme**: Dark / Cyberpunk / Clean.
- **Effects**: Blur background, glow effects on focus.
