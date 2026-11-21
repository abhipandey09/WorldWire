import { WeddingEvent, Venue } from '../types';

export const WEDDING_COUPLE = {
  bride: 'Sakshi',
  groom: 'Abhishek',
  title: 'Sakshi & Abhishek',
  tagline: 'Two Souls, One Beautiful Journey',
  invitationMantra: '॥ श्री गणेशाय नमः ॥',
  subMantra: '॥ श्री जीण माता नमः ॥',
  invitationText: 'Together with their families, cordially invite you to celebrate the auspicious wedding of their children.',
  weddingDate: '26 & 27 January 2027',
  location: 'Bengaluru, Karnataka',
  closingBlessing: '“Your gracious presence will blossom our celebrations into cherished memories for a lifetime.”',
  credit: 'Design & Developed by Abhishek'
};

export const FAMILY_DETAILS = {
  bride: {
    name: 'Sakshi',
    title: 'Bride',
    parents: 'Pushpa Devi & Shri Ram Sikaria',
    grandparents: 'Lt. Gayatri Devi & Lt. Arjun Lal Sikaria',
    blessingQuote: 'May your journey together be showered with divine grace and eternal happiness.'
  },
  groom: {
    name: 'Abhishek',
    title: 'Groom',
    parents: 'Smt. Sunita & Sri Maheshwar Pandey',
    grandparents: 'Lt. Saraswati Devi & Lt. Madan Mohan Pandey',
    blessingQuote: 'Two families united in shared love, timeless values, and lifelong blessings.'
  }
};

export const WEDDING_VENUES: Venue[] = [
  {
    id: 'imperial',
    name: 'Imperial Jenukaal Suits',
    tagline: 'Home to all Pre-Wedding Ceremonies (Jan 26 & 27)',
    eventsHosted: ['Mehendi Ceremony', 'Bhaat Ceremony', 'Tilak & Sangeet', 'Haldi Ceremony'],
    addressLine1: '15, Kasavanahalli Main Road, Owners Court Layout,',
    addressLine2: 'Kasavanahalli,',
    cityStateZip: 'Bengaluru – 560035 (Karnataka)',
    fullAddress: '15, Kasavanahalli Main Road, Owners Court Layout, Kasavanahalli, Bengaluru – 560035, Karnataka',
    mapsUrl: 'https://www.google.com/maps/search/?api=1&query=Imperial+Jenukaal+Suits+15+Kasavanahalli+Main+Road+Bengaluru+560035',
    embedQuery: 'Imperial Jenukaal Suits Kasavanahalli Bengaluru'
  },
  {
    id: 'icon',
    name: 'ICON PREMIER HOTEL',
    tagline: 'Venue for Barat, Wedding Ceremony & Grand Reception (Jan 27)',
    eventsHosted: ['Barat & Swagat', 'The Wedding Ceremony', 'Grand Reception & Dinner'],
    addressLine1: '57, 1A, Outer Ring Road, Opp. Sakra World Hospital,',
    addressLine2: 'Devarabisanahalli, Bellandur,',
    cityStateZip: 'Bengaluru – 560103 (Karnataka)',
    fullAddress: '57, 1A, Outer Ring Road, Opp. Sakra World Hospital, Devarabisanahalli, Bellandur, Bengaluru – 560103, Karnataka',
    mapsUrl: 'https://www.google.com/maps/search/?api=1&query=ICON+Premier+Hotel+Outer+Ring+Road+Bellandur+Bengaluru+560103',
    embedQuery: 'ICON Premier Hotel Bellandur Outer Ring Road Bengaluru'
  }
];

export const WEDDING_EVENTS: WeddingEvent[] = [
  {
    id: 'mehendi',
    name: 'Mehendi Ceremony',
    subtitle: 'Henna, Rhythms & Joyful Beginnings',
    dateStr: 'Tuesday, 26 January 2027',
    timeStr: '9:00 AM ONWARDS',
    isoDateTime: '2027-01-26T09:00:00+05:30',
    venueId: 'imperial',
    venueName: 'Imperial Jenukaal Suits',
    venueShort: 'Kasavanahalli, Bengaluru',
    venueAddress: '15, Kasavanahalli Main Road, Owners Court Layout, Kasavanahalli, Bengaluru – 560035',
    mapsUrl: 'https://www.google.com/maps/search/?api=1&query=Imperial+Jenukaal+Suits+15+Kasavanahalli+Main+Road+Bengaluru+560035',
    themeColor: '#164B35', // Emerald Green
    accentColor: '#FFB800', // Marigold Yellow
    bgGradient: 'from-[#0D3323] via-[#164B35] to-[#0A261A]',
    textColor: '#FFF8E8',
    quote: '“Celebrating love, laughter, and new beginnings with the deep hues of sacred henna.”',
    description: 'An auspicious morning filled with fresh aromatic mehendi designs, traditional Rajasthani and Bollywood tunes, laughter, and vibrant marigolds by the poolside.',
    iconName: 'flower',
    cardImage: '/assets/cards/Slide_04_Mehendi.jpg'
  },
  {
    id: 'bhaat',
    name: 'Bhaat Ceremony',
    subtitle: 'Sacred Blessings & Maternal Love',
    dateStr: 'Tuesday, 26 January 2027',
    timeStr: '12:30 PM ONWARDS',
    isoDateTime: '2027-01-26T12:30:00+05:30',
    venueId: 'imperial',
    venueName: 'Imperial Jenukaal Suits',
    venueShort: 'Kasavanahalli, Bengaluru',
    venueAddress: '15, Kasavanahalli Main Road, Owners Court Layout, Kasavanahalli, Bengaluru – 560035',
    mapsUrl: 'https://www.google.com/maps/search/?api=1&query=Imperial+Jenukaal+Suits+15+Kasavanahalli+Main+Road+Bengaluru+560035',
    themeColor: '#B06375', // Royal Pink
    accentColor: '#C6A15B', // Antique Gold
    bgGradient: 'from-[#4D1826] via-[#73273D] to-[#360F1A]',
    textColor: '#FFF8E8',
    quote: '“Sacred family blessings and cherished traditional customs celebrating eternal maternal bonds.”',
    description: 'A deeply emotional traditional ceremony honoring family heritage, where maternal uncles and grandparents shower the bride and groom with blessings, auspicious gifts, and love.',
    iconName: 'sparkles',
    cardImage: '/assets/cards/Slide_05_Bhaat.jpg'
  },
  {
    id: 'sangeet',
    name: 'Tilak & Sangeet Ceremony',
    subtitle: 'A Starry Night of Music, Dance & Glitz',
    dateStr: 'Tuesday, 26 January 2027',
    timeStr: '6:00 PM ONWARDS',
    isoDateTime: '2027-01-26T18:00:00+05:30',
    venueId: 'imperial',
    venueName: 'Imperial Jenukaal Suits',
    venueShort: 'Kasavanahalli, Bengaluru',
    venueAddress: '15, Kasavanahalli Main Road, Owners Court Layout, Kasavanahalli, Bengaluru – 560035',
    mapsUrl: 'https://www.google.com/maps/search/?api=1&query=Imperial+Jenukaal+Suits+15+Kasavanahalli+Main+Road+Bengaluru+560035',
    themeColor: '#C6A15B', // Champagne Gold
    accentColor: '#D98B9C', // Rose Pink
    bgGradient: 'from-[#141B2D] via-[#1E293B] to-[#0F172A]',
    textColor: '#FFF8E8',
    quote: '“Join us for an evening of music, dance, and endless joy as we celebrate love, laughter, and the beginning of their forever.”',
    description: 'Step into an enchanting evening illuminated by fairy lights, pulsating dholak beats, dazzling family dance performances, and musical celebrations under the starry Bengaluru sky.',
    iconName: 'music',
    cardImage: '/assets/cards/Slide_06_Sangeet.jpg'
  },
  {
    id: 'haldi',
    name: 'Haldi Ceremony',
    subtitle: 'Sun-Kissed Turmeric & Joyful Blessings',
    dateStr: 'Wednesday, 27 January 2027',
    timeStr: '9:00 AM ONWARDS',
    isoDateTime: '2027-01-27T09:00:00+05:30',
    venueId: 'imperial',
    venueName: 'Imperial Jenukaal Suits',
    venueShort: 'Kasavanahalli, Bengaluru',
    venueAddress: '15, Kasavanahalli Main Road, Owners Court Layout, Kasavanahalli, Bengaluru – 560035',
    mapsUrl: 'https://www.google.com/maps/search/?api=1&query=Imperial+Jenukaal+Suits+15+Kasavanahalli+Main+Road+Bengaluru+560035',
    themeColor: '#F58220', // Turmeric Saffron
    accentColor: '#FDB813', // Sun Yellow
    bgGradient: 'from-[#78350F] via-[#92400E] to-[#451A03]',
    textColor: '#FFF8E8',
    quote: '“Join us for a day filled with love, laughter, flower petals, and lots of golden haldi!”',
    description: 'A vibrant courtyard affair where friends and family anoint the couple with fragrant turmeric paste, shower them in marigold rain, and celebrate radiant auspicious beginnings.',
    iconName: 'sun',
    cardImage: '/assets/cards/Slide_07_Haldi.jpg'
  },
  {
    id: 'wedding',
    name: 'The Wedding & Reception',
    subtitle: 'Sacred Vows, Royal Mandap & Dinner Celebration',
    dateStr: 'Wednesday, 27 January 2027',
    timeStr: 'RECEPTION 7:00 PM ONWARDS',
    isoDateTime: '2027-01-27T19:00:00+05:30',
    venueId: 'icon',
    venueName: 'ICON PREMIER HOTEL',
    venueShort: 'Bellandur, Bengaluru',
    venueAddress: '57, 1A, Outer Ring Road, Opp. Sakra World Hospital, Devarabisanahalli, Bellandur, Bengaluru – 560103',
    mapsUrl: 'https://www.google.com/maps/search/?api=1&query=ICON+Premier+Hotel+Outer+Ring+Road+Bellandur+Bengaluru+560103',
    themeColor: '#800020', // Royal Burgundy
    accentColor: '#C6A15B', // Antique Gold
    bgGradient: 'from-[#540015] via-[#800020] to-[#2B000B]',
    textColor: '#FFF8E8',
    quote: '“A ceremonial affair, full of splendour, cherished memories & promises for a lifetime.”',
    description: 'The pinnacle of our celebration beginning with the lively Barat & Swagat, the bride’s enchanting walk under the floral canopy, the sacred Vedic pheras at the royal palace mandap, followed by an exquisite grand dinner reception.',
    iconName: 'ring',
    cardImage: '/assets/cards/Slide_10_Wedding.jpg'
  }
];

export const STORY_MILESTONES = [
  {
    title: 'The Serendipitous Beginning',
    heading: 'When Destinies Aligned',
    description: 'Like a melody composed by the cosmos, Sakshi and Abhishek first met and discovered a quiet understanding that felt like coming home.',
    icon: 'heart',
    image: '/assets/couple/couple_heart_lake.jpg'
  },
  {
    title: 'Shared Dreams & Two Families',
    heading: 'A Bond Blessed by Ancestors',
    description: 'With shared laughter, deep respect for family traditions, and unspoken promises, two loving families came together in heart and spirit.',
    icon: 'home',
    image: '/assets/couple/couple_boat_backwaters.jpg'
  },
  {
    title: 'The Sacred Vow',
    heading: 'Two Souls, One Forever',
    description: 'Hand in hand, surrounding the sacred Agni with the divine blessings of Lord Ganesha and Jeen Mata, stepping into eternity as one.',
    icon: 'infinity',
    image: '/assets/couple/couple_sunset_proposal.jpg'
  }
];

// Helper: Format Dates for Google Calendar URL
export function getGoogleCalendarUrl(event: WeddingEvent): string {
  const start = new Date(event.isoDateTime);
  const end = new Date(start.getTime() + 3 * 60 * 60 * 1000);
  
  const toUtcString = (d: Date) => d.toISOString().replace(/-|:|\.\d\d\d/g, '');
  
  const title = encodeURIComponent(`${event.name} - Sakshi & Abhishek Wedding`);
  const details = encodeURIComponent(`${event.subtitle}\n\n${event.description}\n\nVenue: ${event.venueName}\nAddress: ${event.venueAddress}`);
  const location = encodeURIComponent(`${event.venueName}, ${event.venueAddress}`);
  
  return `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${title}&dates=${toUtcString(start)}/${toUtcString(end)}&details=${details}&location=${location}&sf=true&output=xml`;
}

// Helper: Format Dates for Outlook Online URL
export function getOutlookCalendarUrl(event: WeddingEvent): string {
  const start = new Date(event.isoDateTime);
  const end = new Date(start.getTime() + 3 * 60 * 60 * 1000);
  
  const title = encodeURIComponent(`${event.name} - Sakshi & Abhishek Wedding`);
  const details = encodeURIComponent(`${event.subtitle}\n\n${event.description}\n\nVenue: ${event.venueName}\nAddress: ${event.venueAddress}`);
  const location = encodeURIComponent(`${event.venueName}, ${event.venueAddress}`);
  
  return `https://outlook.live.com/calendar/0/deeplink/compose?subject=${title}&body=${details}&location=${location}&startdt=${start.toISOString()}&enddt=${end.toISOString()}`;
}

// Helper: Downloadable .ICS file (Apple Calendar, Outlook Desktop, Android)
export function downloadIcsFile(event: WeddingEvent) {
  const start = new Date(event.isoDateTime);
  const end = new Date(start.getTime() + 3 * 60 * 60 * 1000);
  
  const formatICSDate = (d: Date) => {
    return d.toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';
  };

  const icsContent = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//Sakshi & Abhishek Wedding//Digital Invitation//EN',
    'CALSCALE:GREGORIAN',
    'METHOD:PUBLISH',
    'BEGIN:VEVENT',
    `UID:wedding-${event.id}-2027@mytomboy360.com`,
    `DTSTAMP:${formatICSDate(new Date())}`,
    `DTSTART:${formatICSDate(start)}`,
    `DTEND:${formatICSDate(end)}`,
    `SUMMARY:${event.name} - Sakshi & Abhishek Wedding`,
    `DESCRIPTION:${event.subtitle} \\n\\n${event.description} \\n\\nVenue: ${event.venueName} \\nAddress: ${event.venueAddress}`,
    `LOCATION:${event.venueName}\\, ${event.venueAddress}`,
    'STATUS:CONFIRMED',
    'SEQUENCE:0',
    'END:VEVENT',
    'END:VCALENDAR'
  ].join('\r\n');

  const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
  const url = window.URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.setAttribute('download', `${event.id}_sakshi_abhishek_wedding.ics`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  window.URL.revokeObjectURL(url);
}
