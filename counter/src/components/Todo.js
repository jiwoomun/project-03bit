import React, {useState} from 'react'

const Todo = () => {
    const[ item, setItem ] = useState('')
    return (<>
    <h1> TODO LIST </h1>
    <h4> {item} </h4>


    TODO
    <input onChange = {e => setItem(e.target.value) }/> <br/>

<button onClick = { () => {setItem('')} }> 초기화 </button>
    </>)
}

export default Todo