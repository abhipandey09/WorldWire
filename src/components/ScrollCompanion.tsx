import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ChevronDown, ArrowUp } from 'lucide-react';

const SECTIONS = [
  { id: 'hero', label: 'Home' },
  { id: 'ceremonies', label: 'Ceremonies' },
  { id: 'story', label: 'Our Story' },
  { id: 'venues', label: 'Venues' },
  { id: 'family', label: 'Family' },
  { id: 'film', label: 'Wedding Film' },
  { id: 'footer', label: 'Blessings' },
];

export const ScrollCompanion: React.FC = () => {
  const [currentIdx, setCurrentIdx] = useState(0);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const scrollPos = window.scrollY + 280;
      setIsVisible(window.scrollY > 200);

      for (let i = SECTIONS.length - 1; i >= 0; i--) {
        const el = document.getElementById(SECTIONS[i].id);
        if (el && el.offsetTop <= scrollPos) {
          setCurrentIdx(i);
          break;
        }
      }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleNextScroll = () => {
    if (currentIdx >= SECTIONS.length - 1) {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      const nextSection = SECTIONS[currentIdx + 1];
      const el = document.getElementById(nextSection.id);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
      }
    }
  };

  const isLast = currentIdx >= SECTIONS.length - 1;
  const nextLabel = isLast ? 'Top' : SECTIONS[currentIdx + 1]?.label || 'Next';

  return (
    <AnimatePresence>
      {isVisible && (
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 15 }}
          className="fixed bottom-6 left-3 sm:left-6 z-40"
        >
          <button
            onClick={handleNextScroll}
            className="flex items-center gap-1.5 px-3 py-2 sm:px-3.5 sm:py-2.5 rounded-full bg-ivory/95 hover:bg-champagne border border-gold/70 text-burgundy shadow-xl backdrop-blur-md font-cinzel text-xs font-bold tracking-wider transition-all hover:scale-105 active:scale-95 cursor-pointer"
            title={`Scroll to ${nextLabel}`}
          >
            {isLast ? (
              <>
                <ArrowUp className="w-3.5 h-3.5 text-gold" />
                <span className="text-[10px] sm:text-[11px]">Back to Top</span>
              </>
            ) : (
              <>
                <span className="text-[10px] sm:text-[11px] text-[#5C453C]">Scroll: {nextLabel}</span>
                <ChevronDown className="w-3.5 h-3.5 text-burgundy animate-bounce" />
              </>
            )}
          </button>
        </motion.div>
      )}
    </AnimatePresence>
  );
};
