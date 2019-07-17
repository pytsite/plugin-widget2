import PropTypes from 'prop-types';
import React from 'react';

export default class Widget extends React.Component {
    static propTypes = {
        className: PropTypes.string,
        id: PropTypes.string.isRequired,
    };
}
