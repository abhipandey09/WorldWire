import React, { useState, useEffect } from 'react';
import { Volume2, VolumeX, Menu, X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface NavbarProps {
  isPlaying: boolean;
  onToggleMusic: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({ isPlaying, onToggleMusic }) => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 40);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { label: 'Home', href: '#hero' },
    { label: 'Ceremonies', href: '#ceremonies' },
    { label: 'Our Story', href: '#story' },
    { label: 'Venues', href: '#venues' },
    { label: 'Family', href: '#family' },
    { label: 'Wedding Film', href: '#film' },
  ];

  const handleLinkClick = (href: string) => {
    setIsMobileMenuOpen(false);
    const element = document.querySelector(href);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <>
      <header
        className={`fixed top-0 left-0 right-0 z-40 transition-all duration-500 ${
          isScrolled
            ? 'bg-ivory/90 backdrop-blur-md shadow-md border-b border-gold/30 py-2.5'
            : 'bg-transparent py-4'
        }`}
      >
        <div className="max-w-6xl mx-auto px-4 sm:px-6 flex items-center justify-between">
          {/* Logo / Monogram */}
          <a
            href="#hero"
            onClick={(e) => {
              e.preventDefault();
              handleLinkClick('#hero');
            }}
            className="flex items-center gap-2 group"
          >
            <div className="w-10 h-10 rounded-full border border-gold/70 overflow-hidden shadow-sm group-hover:scale-105 transition-transform flex items-center justify-center bg-[#3D0A14]">
              <img
                src="/assets/logos/sa_logo.jpg"
                alt="SA Monogram"
                className="w-full h-full object-cover"
              />
            </div>
            <div className="flex flex-col">
              <span className="font-cinzel font-bold text-xs sm:text-sm tracking-widest text-burgundy">
                SAKSHI &amp; ABHISHEK
              </span>
              <span className="text-[10px] tracking-wider text-[#7A5A4A] font-cormorant italic">
                26 &amp; 27 January 2027
              </span>
            </div>
          </a>

          {/* Desktop Navigation Links */}
          <nav className="hidden md:flex items-center gap-6">
            {navLinks.map((link) => (
              <a
                key={link.label}
                href={link.href}
                onClick={(e) => {
                  e.preventDefault();
                  handleLinkClick(link.href);
                }}
                className="font-cinzel text-xs font-semibold tracking-wider text-[#4A352D] hover:text-burgundy transition-colors relative py-1 after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-0 after:h-[1.5px] after:bg-gold hover:after:w-full after:transition-all after:duration-300"
              >
                {link.label}
              </a>
            ))}
          </nav>

          {/* Actions: Music Toggle & Mobile Menu Trigger */}
          <div className="flex items-center gap-2.5">
            <button
              onClick={onToggleMusic}
              title={isPlaying ? 'Pause Indian Wedding Music' : 'Play Indian Wedding Music'}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-champagne/80 hover:bg-champagne border border-gold/40 text-burgundy text-xs font-cinzel font-semibold shadow-sm transition-all hover:scale-105 active:scale-95"
            >
              {isPlaying ? (
                <>
                  <Volume2 className="w-4 h-4 text-burgundy animate-pulse" />
                  <span className="hidden sm:inline text-[11px]">Music Playing</span>
                </>
              ) : (
                <>
                  <VolumeX className="w-4 h-4 text-[#8C6D60]" />
                  <span className="hidden sm:inline text-[11px] text-[#8C6D60]">Play Music</span>
                </>
              )}
            </button>

            {/* Mobile Hamburger Toggle */}
            <button
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              className="md:hidden p-2 rounded-lg text-burgundy hover:bg-gold/10 transition-colors"
              aria-label="Toggle navigation menu"
            >
              {isMobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </header>

      {/* Mobile Drawer Navigation */}
      <AnimatePresence>
        {isMobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.25 }}
            className="fixed inset-x-0 top-16 z-30 md:hidden bg-ivory/95 backdrop-blur-xl border-b border-gold/40 shadow-xl px-6 py-6"
          >
            <div className="flex flex-col gap-4">
              {navLinks.map((link) => (
                <a
                  key={link.label}
                  href={link.href}
                  onClick={(e) => {
                    e.preventDefault();
                    handleLinkClick(link.href);
                  }}
                  className="font-cinzel text-sm font-semibold tracking-wider text-burgundy py-2 border-b border-gold/20 flex items-center justify-between"
                >
                  <span>{link.label}</span>
                  <span className="text-gold text-xs">✦</span>
                </a>
              ))}
              <div className="pt-2 flex justify-center">
                <a
                  href="#ceremonies"
                  onClick={(e) => {
                    e.preventDefault();
                    handleLinkClick('#ceremonies');
                  }}
                  className="w-full text-center py-2.5 rounded-full bg-burgundy text-white font-cinzel text-xs font-bold tracking-widest shadow-md"
                >
                  EXPLORE CEREMONIES
                </a>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
};
