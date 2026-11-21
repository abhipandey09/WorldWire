import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Sparkles, Flower2, Music, Sun, HeartHandshake, ChevronDown } from 'lucide-react';
import { WEDDING_EVENTS } from '../data/weddingData';
import { WeddingEvent } from '../types';
import { EventCard } from './EventCard';
import { EventInvitationModal } from './EventInvitationModal';
import { CalendarModal } from './CalendarModal';

export const FunctionsSection: React.FC = () => {
  const [selectedEventForCard, setSelectedEventForCard] = useState<WeddingEvent | null>(null);
  const [selectedEventForCal, setSelectedEventForCal] = useState<WeddingEvent | null>(null);

  const scrollToStory = () => {
    document.querySelector('#story')?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section id="ceremonies" className="relative py-20 bg-ivory/60 border-t border-b border-gold/30 overflow-hidden">
      {/* Personalized Couple Photo Background: Ring Ceremony Celebrations */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <img
          src="/assets/couple/couple_ring_ceremony_portrait.jpg"
          alt="Sakshi & Abhishek Ring Ceremony"
          className="w-full h-full object-cover object-center opacity-25 sm:opacity-15 filter contrast-[1.05]"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-[#FFFDF9]/85 via-ivory/70 to-[#FFFDF9]/90" />
      </div>

      {/* Background Ambience */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <div className="absolute top-1/3 right-10 w-96 h-96 bg-gold/5 rounded-full blur-3xl" />
        <div className="absolute bottom-1/4 left-10 w-96 h-96 bg-burgundy/5 rounded-full blur-3xl" />
      </div>

      <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6">
        {/* Section Header */}
        <div className="text-center max-w-2xl mx-auto mb-12 sm:mb-16">
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="flex items-center justify-center gap-2 mb-2 text-burgundy font-serif font-bold text-sm tracking-widest uppercase"
          >
            <span className="text-gold">✦</span>
            <span>Auspicious Wedding Ceremonies</span>
            <span className="text-gold">✦</span>
          </motion.div>

          <motion.h2
            initial={{ opacity: 0, y: 15 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1 }}
            className="font-serif font-bold text-3xl sm:text-5xl text-burgundy drop-shadow-sm tracking-tight"
          >
            The Sacred Festivities
          </motion.h2>

          <motion.p
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2 }}
            className="font-cormorant italic text-base sm:text-lg text-[#664E43] mt-2"
          >
            Join us across two days of joyous traditions, music, sacred pheras, and heartfelt memories.
          </motion.p>

          <div className="flex items-center justify-center w-40 mx-auto mt-4">
            <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
            <span className="mx-2 text-gold text-xs">🪷</span>
            <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
          </div>
        </div>

        {/* Day 1: Tuesday, 26 January 2027 Group */}
        <div className="mb-14">
          <div className="flex items-center gap-3 mb-6">
            <div className="w-3 h-3 rotate-45 bg-gold" />
            <h3 className="font-cinzel font-bold text-lg sm:text-xl text-burgundy tracking-wide">
              DAY 1 &bull; TUESDAY, 26 JANUARY 2027
            </h3>
            <div className="h-[1px] flex-1 bg-gold/40" />
            <span className="text-xs text-[#7A5A4A] font-cormorant italic hidden sm:inline">
              Pre-Wedding Festivities
            </span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8">
            {WEDDING_EVENTS.slice(0, 3).map((event) => (
              <EventCard
                key={event.id}
                event={event}
                onViewCard={(ev) => setSelectedEventForCard(ev)}
                onAddCalendar={(ev) => setSelectedEventForCal(ev)}
              />
            ))}
          </div>
        </div>

        {/* Day 2: Wednesday, 27 January 2027 Group */}
        <div className="mb-8">
          <div className="flex items-center gap-3 mb-6">
            <div className="w-3 h-3 rotate-45 bg-gold" />
            <h3 className="font-cinzel font-bold text-lg sm:text-xl text-burgundy tracking-wide">
              DAY 2 &bull; WEDNESDAY, 27 JANUARY 2027
            </h3>
            <div className="h-[1px] flex-1 bg-gold/40" />
            <span className="text-xs text-[#7A5A4A] font-cormorant italic hidden sm:inline">
              The Grand Auspicious Day
            </span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8 max-w-4xl mx-auto">
            {WEDDING_EVENTS.slice(3, 5).map((event) => (
              <EventCard
                key={event.id}
                event={event}
                onViewCard={(ev) => setSelectedEventForCard(ev)}
                onAddCalendar={(ev) => setSelectedEventForCal(ev)}
              />
            ))}
          </div>
        </div>

        {/* Scroll Option to Next Section: Our Journey */}
        <div className="mt-14 flex justify-center">
          <button
            onClick={scrollToStory}
            className="flex flex-col items-center gap-1.5 text-burgundy/80 hover:text-burgundy transition-colors group cursor-pointer"
          >
            <span className="font-cinzel text-xs font-semibold tracking-widest uppercase">
              Continue to Our Journey
            </span>
            <ChevronDown className="w-4 h-4 animate-bounce text-gold" />
          </button>
        </div>
      </div>

      {/* Official Invitation Card Lightbox Modal */}
      <EventInvitationModal
        event={selectedEventForCard}
        onClose={() => setSelectedEventForCard(null)}
        onOpenCalendar={(ev) => setSelectedEventForCal(ev)}
      />

      {/* Calendar Add Options Modal */}
      <CalendarModal
        event={selectedEventForCal}
        onClose={() => setSelectedEventForCal(null)}
      />
    </section>
  );
};
