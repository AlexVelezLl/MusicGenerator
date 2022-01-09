import MuiSlider, { SliderThumb } from '@mui/material/Slider';
import { styled } from '@mui/material/styles';

export const Slider = styled(MuiSlider)(() => ({
  color: 'var(--primary-color)',
  height: 3,
  padding: '13px 0',
  '& .MuiSlider-thumb': {
    height: 27,
    width: 27,
    backgroundColor: '#fff',
    border: '1px solid currentColor',
    '&:hover': {
      boxShadow: '0 0 0 8px rgba(76, 198, 120, 0.16)',
    },
    '&:active': {
      boxShadow: '0 0 0 16px rgba(76, 198, 120, 0.16)',
    },
    '&:focus-visible': {
      boxShadow: '0 0 0 4px rgba(76, 198, 120, 0.16)',
    },
    '& .airbnb-bar': {
      height: 9,
      width: 1,
      backgroundColor: 'currentColor',
      marginLeft: 1,
      marginRight: 1,
    },
  },
  '& .MuiSlider-track': {
    height: 3,
  },
  '& .MuiSlider-rail': {
    color: '#C4C4C4',
    opacity: 1,
    height: 3,
  },
}));

export const SliderThumbComponent = (props) => {
  const { children, ...other } = props;
  return (
    <SliderThumb {...other}>
      {children}
      <span className="airbnb-bar" />
      <span className="airbnb-bar" />
      <span className="airbnb-bar" />
    </SliderThumb>
  );
}