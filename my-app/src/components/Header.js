import React from 'react';

function Header() {
    return (
        <header style={headerStyle}>
            <h1 class="animated bounceInDown">Reddit Optimizer</h1>
        </header>

    )
}

const headerStyle = {
    paddingTop: '5vw',
    paddingBottom: '0.5vw',
    textAlign: 'center',
    fontFamily: 'Quicksand',
    backgroundColor: 'black',
    color:'white',
    fontSize: '30px'
}
export default Header;