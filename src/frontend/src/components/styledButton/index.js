import React from 'react';
import { Button } from 'antd';

const StyledButton = (props) => { 
    let buttonColor = '';
    let textColor = '';
    switch (props.textColor) {
        case 'green':
            buttonColor = '#ADF3A6';
            textColor = 'black';
            break;
        case 'yellow':
            buttonColor = '#F3D56D';
            textColor = 'black';
            break;
        case 'red':
            buttonColor = '#F36D6D';
            textColor = 'black';
            break;
        case 'gray':
            buttonColor = '#D9D9D9';
            textColor = 'black';
            break;
        case 'blue':
            buttonColor = 'linear-gradient(to right, #23B6E6, #B5E4E4)';
            textColor = 'black';
            break;
        case 'purple':
            buttonColor = 'linear-gradient(to right, #8404FC, #A587EB)';
            textColor = 'white';
            break;
        default:
            buttonColor = 'blue';
            break;
    }
    return (
        <Button  
        style={{ background: buttonColor, color: textColor, minHeight:"8vh", minWidth:"10vw", borderRadius:"25"}} 
        onClick={props.onClick}>{props.text}</Button>
    );}

export default StyledButton;