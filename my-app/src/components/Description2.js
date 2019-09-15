import React from 'react';

function Description() {
    return (
        <header style={desStyle}>
            <p>We predit that these are the top 5 subreddits that will get you the most karma.</p>
        </header>

    )
}

const desStyle = {
    padding: '0.5vw 4vw',
    paddingBottom: '3vw',
    textAlign: 'center',
    fontFamily: 'Quicksand',
    fontSize: '25px',
    backgroundColor: 'black',
    color: 'white',
}
export default Description;