// frontend/src/components/Accordion.tsx

import React, { useState } from 'react';
import './Accordion.css';

interface AccordionProps {
    title: string;
    children: React.ReactNode;
}

const Accordion: React.FC<AccordionProps> = ({ title, children }) => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleAccordion = () => {
        setIsOpen(!isOpen);
    };

    return (
        <div className="accordion">
            <button className="accordion-button" onClick={toggleAccordion}>
                {title} {isOpen ? '-' : '+'}
            </button>
            {isOpen && <div className="accordion-content">{children}</div>}
        </div>
    );
};

export default Accordion;
