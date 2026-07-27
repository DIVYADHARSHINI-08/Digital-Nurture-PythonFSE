import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)



// basics notes :
/*
Browser

↓

index.html

↓

main.jsx

↓

<App/>

↓

App.jsx

↓

Header.jsx
CourseCard.jsx
Footer.jsx

↓

HTML generated

↓

Browser displays page
*/