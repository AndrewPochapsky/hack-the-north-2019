import React from 'react';

function Header() {
    return (
        <header style={headerStyle}>
            <h1>Reddit Optimizer</h1>
        </header>

    )
}

const headerStyle = {
    paddingTop: '5vw',
    paddingBottom: '0.5vw',
    textAlign: 'center',
    fontFamily: 'Quicksand',
    backgroundColor: '#d6d6f5',
    fontSize: '30px'
}
export default Header;