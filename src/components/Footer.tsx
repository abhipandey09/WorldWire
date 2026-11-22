import React from 'react';
import { Heart, Sparkles, ArrowUp } from 'lucide-react';
import { WEDDING_COUPLE } from '../data/weddingData';

export const Footer: React.FC = () => {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer id="footer" className="relative bg-[#1A0B0F] text-ivory py-16 border-t-2 border-gold/50 overflow-hidden">
      {/* Personalized Couple Photo Background: Romantic Forever */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <img
          src="/assets/couple/couple_romantic_embrace.jpg"
          alt="Sakshi & Abhishek Forever"
          className="w-full h-full object-cover object-top opacity-15 filter brightness-75 contrast-125"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-[#1A0B0F]/90 via-[#1A0B0F]/75 to-[#1A0B0F]" />
      </div>

      {/* Background Golden Glow */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-[320px] sm:w-[600px] h-64 bg-gold/10 rounded-full blur-[80px] sm:blur-[100px]" />
      </div>

      <div className="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 text-center flex flex-col items-center">
        {/* Sacred Sub Mantra */}
        <div className="text-gold font-serif font-bold text-sm tracking-widest mb-3">
          {WEDDING_COUPLE.subMantra}
        </div>

        {/* Monogram */}
        <div className="w-20 h-20 sm:w-24 sm:h-24 rounded-full border-2 border-gold/80 overflow-hidden shadow-gold-glow mb-4 flex items-center justify-center bg-[#3D0A14]">
          <img
            src="/assets/logos/sa_logo.jpg"
            alt="SA Monogram"
            className="w-full h-full object-cover"
          />
        </div>

        {/* Couple Names */}
        <h2 className="font-script text-4xl sm:text-6xl text-gold font-normal mb-2 drop-shadow">
          Sakshi <span className="font-serif text-2xl sm:text-3xl text-white/80">&amp;</span> Abhishek
        </h2>

        {/* Closing Blessing */}
        <p className="max-w-xl font-cormorant italic text-base sm:text-lg text-champagne/90 my-3 px-4 leading-relaxed">
          {WEDDING_COUPLE.closingBlessing}
        </p>

        {/* Dates & Location */}
        <p className="font-cinzel text-xs font-semibold text-gold/80 tracking-widest uppercase mt-2">
          {WEDDING_COUPLE.weddingDate} &bull; {WEDDING_COUPLE.location}
        </p>

        {/* Golden Flourish Divider */}
        <div className="flex items-center justify-center w-48 my-6">
          <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
          <span className="mx-2 text-gold text-xs">✦</span>
          <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
        </div>

        {/* Mandatory Requested Credit: Design & Developed by Abhishek */}
        <div className="py-2.5 px-6 rounded-full bg-burgundy/60 border border-gold/40 shadow-inner my-2">
          <p className="font-cinzel font-bold text-xs sm:text-sm tracking-wider text-gold flex items-center justify-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5 text-gold" />
            <span>Design &amp; Developed by Abhishek</span>
            <Sparkles className="w-3.5 h-3.5 text-gold" />
          </p>
        </div>

        {/* Domain Reference */}
        <p className="text-[11px] text-white/50 font-sans mt-3">
          &copy; 2027 &bull; Official Digital Wedding Invitation &bull;{' '}
          <a
            href="https://mytomboy360.com"
            className="text-gold/80 hover:text-gold underline transition-colors"
          >
            mytomboy360.com
          </a>
        </p>

        {/* Back to Top Button */}
        <button
          onClick={scrollToTop}
          className="mt-8 flex items-center gap-1 text-xs text-gold/70 hover:text-gold font-cinzel tracking-wider transition-colors"
        >
          <span>Back to Top</span>
          <ArrowUp className="w-3.5 h-3.5" />
        </button>
      </div>
    </footer>
  );
};
