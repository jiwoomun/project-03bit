import React from 'react'

const Counter = () => {
    const onAddClick = () => {
        alert('+ 클릭')
    }
    const onSubClick = () => {
        alert('+ 클릭')
    }
    return(<>
    <h1>카운터</h1>
    <button onClick = {onAddClick}> + </button>
    <button onClick = {onSubClick}> - </button>
    </>)
}

export default Counter