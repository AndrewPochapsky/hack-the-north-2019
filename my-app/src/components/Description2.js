import React from 'react';

function Description() {
    return (
        <header style={desStyle}>
            <p>Here's the after screen</p>
        </header>

    )
}

const desStyle = {
    padding: '0.5vw 4vw',
    paddingBottom: '5vw',
    textAlign: 'center',
    fontFamily: 'Quicksand',
    fontSize: '25px',
    backgroundColor: 'black',
    color: 'white',
}
export default Description;