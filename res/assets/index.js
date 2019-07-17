import React from "react";
import ReactDOM from "react-dom";
import {Html} from "./components/static";
import Input from "./components/input";

const widgets = {};

/**
 * Register widget
 *
 * @param {string} cid
 * @param {Rect.Component} widgetComponent
 */
export function registerWidget(cid, widgetComponent) {
    widgets[cid] = widgetComponent;
    initComponents(cid);
}

/**
 * Create widget
 *
 * @param {string} cid
 * @param {Object} props
 * @returns {React.Element}
 */
export function createWidget(cid, props) {
    if (!widgets.hasOwnProperty(cid))
        throw `Component for widget '${cid}' is not registered`;

    const children = [];
    if (props.hasOwnProperty('children') && props.children) {
        props.children.forEach(childInfo => {
            children.push(createWidget(childInfo['cid'], childInfo['props']));
        });
    }

    return React.createElement(widgets[cid], props, ...children);
}

/**
 * Hydrate an HTML element with component
 *
 * @param {HTMLElement} node
 */
export function hydrateHTMLElement(node) {
    const cid = node.getAttribute('data-cid');
    const props = JSON.parse(node.getAttribute('data-props'));
    const widget = createWidget(cid, props);

    ReactDOM.render(widget, node);

    // Remove wrapper
    node.children.forEach(childNode => {
        node.parentNode.insertBefore(childNode, node);
    });
    node.remove();
}

/**
 * Initialize non-initialized components found on the page
 *
 * @param {string} cid
 */
function initComponents(cid) {
    document.querySelectorAll(`.pytsite-widget2-container[data-cid="${cid}"]`).forEach(em => {
        hydrateHTMLElement(em)
    });
}

// Register widgets provided by this plugin
registerWidget('plugins.widget2.static.html', Html);

registerWidget('plugins.widget2.input.input', Input);
registerWidget('plugins.widget2.input.hidden', Input);
registerWidget('plugins.widget2.input.text', Input);
registerWidget('plugins.widget2.input.submit', Input);
