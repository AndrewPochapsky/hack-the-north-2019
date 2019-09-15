import React from 'react';

function Description() {
    return (
        <header style={desStyle}>
            <p>Copy and Paste your reddit post into the text box. We will tell you the top 5 subreddits that will give your post the most traction.</p>
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
