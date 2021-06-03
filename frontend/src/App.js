import React from 'react'
import { BrowserRoutera as Router, Link } from "react-router"

const App = () => {
  return (<>
  
  <nav>
    <Link to="./">Home</Link>
    <Link to="./">Blog</Link>
    <Link to="./">Home</Link>
  </nav>

  <h1>첫번째 크기 헤드라인</h1>
  <h2>두번째 크기 헤드라인</h2>
  <h3>첫번째 크기 헤드라인</h3>
  <h4>첫번째 크기 헤드라인</h4>
  <h5>첫번째 크기 헤드라인</h5>
  <p>문단은 p로 쓰세요. p는 아마도 Paragraph의 앞글자를 따온 것이겠죠?</p>
  <hr/>
  <img src=".src/image/stay_funky.jpg" width="600px"></img>

  </>)
}

export default App