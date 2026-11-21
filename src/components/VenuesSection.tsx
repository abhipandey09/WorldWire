import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { MapPin, Navigation, ExternalLink, Calendar, CheckCircle2 } from 'lucide-react';
import { WEDDING_VENUES } from '../data/weddingData';

export const VenuesSection: React.FC = () => {
  const [activeVenueTab, setActiveVenueTab] = useState<'imperial' | 'icon'>('imperial');

  return (
    <section id="venues" className="relative py-20 bg-[#FFFDF9]">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        {/* Section Header */}
        <div className="text-center max-w-2xl mx-auto mb-12">
          <div className="flex items-center justify-center gap-2 mb-2 text-burgundy font-serif font-bold text-sm tracking-widest uppercase">
            <span className="text-gold">✦</span>
            <span>Where to Celebrate</span>
            <span className="text-gold">✦</span>
          </div>

          <h2 className="font-serif font-bold text-3xl sm:text-5xl text-burgundy tracking-tight">
            Wedding Venues
          </h2>

          <p className="font-cormorant italic text-base sm:text-lg text-[#6E4F41] mt-2">
            Two magnificent locations in Bengaluru, Karnataka carefully chosen to host our celebrations.
          </p>

          <div className="flex items-center justify-center w-36 mx-auto mt-4">
            <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
            <span className="mx-2 text-gold text-xs">🏛️</span>
            <div className="h-[1px] flex-1 bg-gradient-to-r from-transparent via-gold to-transparent" />
          </div>
        </div>

        {/* Venue Cards Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
          {WEDDING_VENUES.map((venue, idx) => (
            <motion.div
              key={venue.id}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: idx * 0.2, duration: 0.7 }}
              className="relative flex flex-col justify-between rounded-2xl p-6 sm:p-8 bg-ivory border-2 border-gold/50 shadow-lg hover:shadow-gold-glow transition-all duration-300"
            >
              {/* Inner subtle filigree border */}
              <div className="absolute inset-2 border border-gold/25 rounded-xl pointer-events-none" />

              <div>
                {/* Top Badge */}
                <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-burgundy/10 text-burgundy text-xs font-cinzel font-bold mb-4">
                  <MapPin className="w-3.5 h-3.5 text-burgundy" />
                  <span>VENUE {idx + 1} OF 2</span>
                </div>

                {/* Venue Name */}
                <h3 className="font-serif font-bold text-2xl sm:text-3xl text-burgundy">
                  {venue.name}
                </h3>
                <p className="font-cormorant italic text-sm sm:text-base text-gold font-semibold mb-4">
                  {venue.tagline}
                </p>

                {/* Physical Address */}
                <div className="p-4 rounded-xl bg-champagne/40 border border-gold/40 text-xs sm:text-sm text-[#423129] my-4 leading-relaxed">
                  <p className="font-semibold text-burgundy">{venue.addressLine1}</p>
                  <p>{venue.addressLine2}</p>
                  <p className="font-semibold">{venue.cityStateZip}</p>
                </div>

                {/* Ceremonies Hosted at this venue */}
                <div className="my-4">
                  <span className="font-cinzel text-xs font-bold tracking-wider text-burgundy uppercase block mb-2">
                    Ceremonies Hosted Here:
                  </span>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                    {venue.eventsHosted.map((evName) => (
                      <div
                        key={evName}
                        className="flex items-center gap-2 p-2 rounded-lg bg-white/80 border border-gold/30 text-xs text-[#523E35]"
                      >
                        <CheckCircle2 className="w-3.5 h-3.5 text-gold shrink-0" />
                        <span className="font-medium">{evName}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Highlights */}
                <div className="flex flex-wrap gap-1.5 my-3">
                  {venue.highlights.map((item) => (
                    <span
                      key={item}
                      className="text-[11px] px-2.5 py-0.5 rounded-full bg-gold/15 text-[#634B28] font-sans"
                    >
                      &bull; {item}
                    </span>
                  ))}
                </div>
              </div>

              {/* Action Buttons */}
              <div className="pt-6 border-t border-gold/30 flex flex-wrap gap-3 mt-6">
                <a
                  href={`https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(venue.fullAddress)}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex-1 flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-burgundy hover:bg-burgundy/90 text-white font-cinzel font-bold text-xs tracking-wider shadow-md hover:scale-[1.02] active:scale-[0.98] transition-all"
                >
                  <Navigation className="w-4 h-4 text-gold" />
                  <span>Get Driving Directions</span>
                </a>

                <a
                  href={venue.mapsUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center justify-center gap-1.5 px-4 py-3 rounded-xl bg-champagne hover:bg-gold/20 border border-gold/60 text-burgundy font-cinzel font-bold text-xs tracking-wider transition-all"
                >
                  <ExternalLink className="w-4 h-4" />
                  <span>Open Maps</span>
                </a>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};
