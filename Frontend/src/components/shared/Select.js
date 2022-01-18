import React from 'react';
import ReactSelect from 'react-select';

const customSelectStyles = {
  option: (provided, state) => ({
    ...provided,
    color: state.isSelected ? 'white' : 'black',
    backgroundColor: state.isSelected ? 'var(--primary-color)' : 'white',
  }),
  control: (provided, state) => ({
    ...provided,
    border: 'none',
    boxShadow: state.isFocused? 'var(--primary-color) 0 0 0 1px' : 'none',
    backgroundColor: '#C4C4C4',
    borderRadius: 10,
    width: '120px'
  }),
  singleValue: (provided) => ({
    ...provided,
    color: 'black',
  }),
  indicatorSeparator: (provided) => ({
    ...provided,
    backgroundColor: '#909090',
  }),
  dropdownIndicator: (provided) => ({
    ...provided,
    color: '#909090',
  }),
}

const Select = (props) => {
  return (
    <ReactSelect
      styles={customSelectStyles}
      {...props}
    />
  );
}

export default Select;