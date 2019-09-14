import React, { Component } from 'react'

export class AddPost extends Component {
    render() {
        return (
            <form style={{ display: 'flex' }}>
                <input 
                    type="text"
                    name="title"
                    style={{ padding:'5px', flex: '10', height:'1vw' }}
                    placeholder="Title of your post ..."
                />
                <input
                    type="text"
                    name="description"
                    style={{ padding: '5px', flex: '10', height:'10vw' }}
                    placeholder="Insert your post content here ..."
                />
                <input
                    type="submit"
                    value="submit"
                    className="btn"
                />
            </form>
        )
    }
}
export default AddPost