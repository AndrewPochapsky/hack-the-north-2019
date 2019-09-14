import React, { Component } from 'react'

export class AddPost extends Component {
    state = {
        title: '',
        description: ''
    }

    onSubmit = (e) => {
        e.preventDefault();     //prevent it from submitting to default thing
        //ADD CODE THAT STORES THIS SOMEWHERE
        this.setState({ title: '', description: '' });
    }

    onChange = (e) => this.setState({ [e.target.name]: e.target.value });

    render() {
        return (
            <form onSubmit={this.onSubmit} style={formSty}>
                <label style={labelSty}>
                Title:
                <input 
                        type="text"
                        name="title"
                        style={textSty}
                        placeholder="Title of your post ..."
                        value={this.state.title}
                        onChange={this.onChange}
                    />
                </label>   
                <label style={labelSty}>
                    Body:
                <input
                        type="text"
                        name="description"
                        style={textSty}
                        placeholder="Insert your post content here ..."
                        value={this.state.description}
                        onChange={this.onChange}
                    />
                    </label>
                <input
                    type="submit"
                    value="submit"
                    style={buttonSty}
                    className="btn"
                />
            </form>
        )
    }
}

const formSty = {
    backgroundColor: 'black',
    color: 'white',
    paddingLeft: '20vw',
    paddingRight: '20vw'
}

const labelSty = {
    paddingRight: '5vw',
    fontFamily: 'Quicksand',
    fontSize: '25px'
}

const textSty = {
    width: '100%',
    padding: '4vw',
   // borderRadius: '10%',
    marginBottom: '5vw',
    backgroundColor: '#d9d9d9'
}

const buttonSty = {
    backgroundColor: '#595959',
    padding: '2vw 2vw',
    borderRadius: '30%',
    color: 'white',
    fontSize:'25px',
    //float: 'right'
}

export default AddPost