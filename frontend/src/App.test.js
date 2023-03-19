import { render, screen } from '@testing-library/react';
import App from './App';

test('renders search bar', () => {
    render(<App />);
    const linkElement = screen.getByText(/enter patient ID:/i);
    expect(linkElement).toBeInTheDocument();
});
