import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Calendar, Clock, MapPin, Eye, Navigation, Sparkles, Shirt } from 'lucide-react';
import { WeddingEvent } from '../types';

interface EventCardProps {
  event: WeddingEvent;
  onViewCard: (event: WeddingEvent) => void;
  onAddCalendar: (event: WeddingEvent) => void;
}

export const EventCard: React.FC<EventCardProps> = ({
  event,
  onViewCard,
  onAddCalendar,
}) => {
  const [isExpanded, setIsExpanded] = useState(false);
  const [daysRemaining, setDaysRemaining] = useState<number | null>(null);

  useEffect(() => {
    const now = new Date().getTime();
    const eventTime = new Date(event.isoDateTime).getTime();
    const diffDays = Math.ceil((eventTime - now) / (1000 * 60 * 60 * 24));
    setDaysRemaining(diffDays);
  }, [event.isoDateTime]);

  return (
    <motion.div
      initial={{ opacity: 0, y: 35 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-50px' }}
      transition={{ duration: 0.7 }}
      className="group relative rounded-2xl overflow-hidden shadow-xl border border-gold/50 bg-gradient-to-b from-[#FFFDF9] via-[#FAF3E6] to-[#F5EAD4] hover:shadow-gold-glow transition-all duration-500"
    >
      {/* Decorative Top Accent Header Bar with Ceremony Theme Color */}
      <div
        className="h-2.5 w-full"
        style={{
          background: `linear-gradient(90deg, ${event.themeColor}, ${event.accentColor}, ${event.themeColor})`,
        }}
      />

      <div className="p-5 sm:p-7 flex flex-col justify-between h-full">
        {/* Top Info: Date Badge & Ceremony Countdown Tag */}
        <div>
          <div className="flex items-center justify-between gap-2 mb-3">
            <span
              className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-cinzel font-bold tracking-wider"
              style={{
                backgroundColor: `${event.themeColor}15`,
                color: event.themeColor,
                border: `1px solid ${event.themeColor}35`,
              }}
            >
              <Calendar className="w-3.5 h-3.5" />
              <span>{event.dateStr}</span>
            </span>

            {daysRemaining !== null && (
              <span className="text-[11px] font-sans font-semibold text-[#7D5F52]">
                {daysRemaining > 0 ? (
                  <span className="text-burgundy font-cinzel font-bold">In {daysRemaining} days</span>
                ) : daysRemaining === 0 ? (
                  <span className="text-emerald-700 font-bold animate-pulse">Today!</span>
                ) : (
                  <span className="text-gray-500">Completed</span>
                )}
              </span>
            )}
          </div>

          {/* Ceremony Title */}
          <h3 className="font-serif font-bold text-2xl sm:text-3xl text-burgundy tracking-tight mt-1 group-hover:text-gold transition-colors duration-300">
            {event.name}
          </h3>

          <p className="font-cormorant italic text-sm sm:text-base text-[#6E4F41] mb-3">
            {event.subtitle}
          </p>

          {/* Poetic Quote */}
          <p className="text-xs sm:text-sm font-cormorant italic text-[#4A3830] bg-gold/10 p-3 rounded-lg border-l-2 border-gold my-3 leading-relaxed">
            {event.quote}
          </p>

          {/* Ceremony Details Grid */}
          <div className="space-y-2.5 text-xs sm:text-sm text-[#4F3B32] my-4">
            <div className="flex items-start gap-2.5">
              <Clock className="w-4 h-4 text-gold shrink-0 mt-0.5" />
              <div>
                <span className="font-bold text-burgundy font-cinzel">{event.timeStr}</span>
              </div>
            </div>

            <div className="flex items-start gap-2.5">
              <MapPin className="w-4 h-4 text-gold shrink-0 mt-0.5" />
              <div>
                <span className="font-semibold text-[#3D2C24]">{event.venueName}</span>
                <p className="text-[11px] text-[#785F54]">{event.venueAddress}</p>
              </div>
            </div>

            {event.dressCode && (
              <div className="flex items-start gap-2.5 pt-1 border-t border-gold/20">
                <Shirt className="w-4 h-4 text-burgundy/70 shrink-0 mt-0.5" />
                <span className="text-[11px] text-[#634C42]">
                  <strong className="text-burgundy">Attire:</strong> {event.dressCode}
                </span>
              </div>
            )}
          </div>
        </div>

        {/* Action Buttons */}
        <div className="pt-4 border-t border-gold/30 flex flex-wrap gap-2">
          {/* View Official Card Button */}
          <button
            onClick={() => onViewCard(event)}
            className="flex-1 flex items-center justify-center gap-1.5 px-3 py-2.5 rounded-xl bg-ivory hover:bg-champagne border border-gold/60 text-burgundy font-cinzel font-bold text-xs tracking-wider shadow-sm hover:scale-[1.02] active:scale-[0.98] transition-all"
          >
            <Eye className="w-3.5 h-3.5 text-gold" />
            <span>View Card</span>
          </button>

          {/* Add to Calendar Button */}
          <button
            onClick={() => onAddCalendar(event)}
            className="flex-1 flex items-center justify-center gap-1.5 px-3 py-2.5 rounded-xl bg-burgundy hover:bg-burgundy/90 text-white font-cinzel font-bold text-xs tracking-wider shadow-sm hover:scale-[1.02] active:scale-[0.98] transition-all"
          >
            <Calendar className="w-3.5 h-3.5 text-gold" />
            <span>Add to Calendar</span>
          </button>

          {/* Get Directions Button */}
          <a
            href={event.mapsUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="p-2.5 rounded-xl bg-champagne hover:bg-gold/20 border border-gold/60 text-burgundy shadow-sm hover:scale-[1.05] active:scale-[0.98] transition-all"
            title="Get Directions in Google Maps"
          >
            <Navigation className="w-4 h-4 text-burgundy" />
          </a>
        </div>
      </div>
    </motion.div>
  );
};
