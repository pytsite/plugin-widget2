import PropTypes from 'prop-types';
import React from 'react';
import Widget from './widget';

export default class Input extends Widget {
    static propTypes = Object.assign({}, Widget.propTypes, {
        autoComplete: PropTypes.string,
        autoFocus: PropTypes.bool,
        disabled: PropTypes.bool,
        form: PropTypes.string,
        list: PropTypes.string,
        name: PropTypes.string,
        onChange: PropTypes.func,
        readOnly: PropTypes.bool,
        required: PropTypes.bool,
        tabIndex: PropTypes.number,
        type: PropTypes.string,
        value: PropTypes.string,
    });

    static defaultProps = {
        type: 'hidden',
    };

    constructor(props) {
        super(props);

        this.state = {
            value: this.props.value,
        };

        this.onChange = this.onChange.bind(this);
    }

    onChange(e) {
        this.setState({value: e.target.value});
        this.props.onChange && this.props.onChange(this.props.id, e);
    }

    render() {
        const props = Object.assign({}, this.props, {onChange: this.onChange});
        return <input {...props}/>;
    }
}
