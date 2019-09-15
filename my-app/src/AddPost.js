import React, { Component } from 'react'

export class AddPost extends Component {
    constructor(props) {
        super(props);
    }

    onChange = (e) => this.setState({ [e.target.name]: e.target.value });

    render() {
        return (
            <form onSubmit={this.props.handleSubmit} style={formSty}>
                <label style={labelSty}>
                Title
                <input
                        type="text"
                        name="title"
                        style={textSty}
                        placeholder="Title of your post ..."
                        value={this.props.title}
                        onChange={this.onChange}
                    />
                </label>
                <label style={labelSty}>
                    Body
                <input
                        type="text"
                        name="description"
                        style={textSty}
                        placeholder="Insert your post content here ..."
                        value={this.props.description}
                        onChange={this.onChange}
                    />
                    </label>
                <input
                    type="submit"
                    value="submit"
                    style={buttonSty}
                    className="btn"
                    htmltype="submit"
                />
            </form>
        )
    }
}



const formSty = {
    backgroundColor: 'black',
    color: 'white',
    paddingLeft: '20vw',
    paddingRight: '20vw',
    paddingBottom: '20vw'
}

const labelSty = {
    paddingRight: '5vw',
    fontFamily: 'Quicksand',
    fontSize: '25px'
}

const textSty = {
    width: '75%',
    padding: '4vw',
    fontFamily: 'Quicksand',
    fontSize: '25px',
    marginBottom: '4vw',
    backgroundColor: '#d9d9d9'
}

const buttonSty = {
    backgroundColor: '#595959',
    width: '150px',
    padding: '15px 0px',
    borderRadius: '30%',
    color: 'white',
    fontSize:'22px',
    float: 'right'
}

export default AddPost
