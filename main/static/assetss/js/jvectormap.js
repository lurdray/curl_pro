!function(t){var e={};function n(r){if(e[r])return e[r].exports;var o=e[r]={i:r,l:!1,exports:{}};return t[r].call(o.exports,o,o.exports,n),o.l=!0,o.exports}n.m=t,n.c=e,n.d=function(t,e,r){n.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:r})},n.r=function(t){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},n.t=function(t,e){if(1&e&&(t=n(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var o in t)n.d(r,o,function(e){return t[e]}.bind(null,o));return r},n.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return n.d(e,"a",e),e},n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},n.p="/",n(n.s=559)}({0:function(t,e,n){(function(e){var n=function(t){return t&&t.Math==Math&&t};t.exports=n("object"==typeof globalThis&&globalThis)||n("object"==typeof window&&window)||n("object"==typeof self&&self)||n("object"==typeof e&&e)||function(){return this}()||Function("return this")()}).call(this,n(58))},1:function(t,e){t.exports=function(t){try{return!!t()}catch(t){return!0}}},10:function(t,e,n){var r=n(39),o=n(15);t.exports=function(t){return r(o(t))}},100:function(t,e,n){var r=n(87),o=n(21),i=n(5)("toStringTag"),a="Arguments"==o(function(){return arguments}());t.exports=r?o:function(t){var e,n,r;return void 0===t?"Undefined":null===t?"Null":"string"==typeof(n=function(t,e){try{return t[e]}catch(t){}}(e=Object(t),i))?n:a?o(e):"Object"==(r=o(e))&&"function"==typeof e.callee?"Arguments":r}},103:function(t,e,n){"use strict";var r,o,i,a=n(97),c=n(9),s=n(2),u=n(5),l=n(41),f=u("iterator"),p=!1;[].keys&&("next"in(i=[].keys())?(o=a(a(i)))!==Object.prototype&&(r=o):p=!0),null==r&&(r={}),l||s(r,f)||c(r,f,(function(){return this})),t.exports={IteratorPrototype:r,BUGGY_SAFARI_ITERATORS:p}},106:function(t,e,n){var r=n(7),o=n(117);t.exports=Object.setPrototypeOf||("__proto__"in{}?function(){var t,e=!1,n={};try{(t=Object.getOwnPropertyDescriptor(Object.prototype,"__proto__").set).call(n,[]),e=n instanceof Array}catch(t){}return function(n,i){return r(n),o(i),e?t.call(n,i):n.__proto__=i,n}}():void 0)},112:function(t,e,n){var r=n(1);t.exports=!r((function(){function t(){}return t.prototype.constructor=null,Object.getPrototypeOf(new t)!==t.prototype}))},116:function(t,e,n){"use strict";var r=n(87),o=n(100);t.exports=r?{}.toString:function(){return"[object "+o(this)+"]"}},117:function(t,e,n){var r=n(4);t.exports=function(t){if(!r(t)&&null!==t)throw TypeError("Can't set "+String(t)+" as a prototype");return t}},12:function(t,e,n){var r=n(20),o=Math.min;t.exports=function(t){return t>0?o(r(t),9007199254740991):0}},122:function(t,e,n){"use strict";var r=n(103).IteratorPrototype,o=n(54),i=n(19),a=n(80),c=n(70),s=function(){return this};t.exports=function(t,e,n){var u=e+" Iterator";return t.prototype=o(r,{next:i(1,n)}),a(t,u,!1,!0),c[u]=s,t}},146:function(t,e,n){"use strict";var r=n(6),o=n(20),i=n(171),a=n(172),c=n(1),s=1..toFixed,u=Math.floor,l=function(t,e,n){return 0===e?n:e%2==1?l(t,e-1,n*t):l(t*t,e/2,n)};r({target:"Number",proto:!0,forced:s&&("0.000"!==8e-5.toFixed(3)||"1"!==.9.toFixed(0)||"1.25"!==1.255.toFixed(2)||"1000000000000000128"!==(0xde0b6b3a7640080).toFixed(0))||!c((function(){s.call({})}))},{toFixed:function(t){var e,n,r,c,s=i(this),f=o(t),p=[0,0,0,0,0,0],g="",m="0",v=function(t,e){for(var n=-1,r=e;++n<6;)r+=t*p[n],p[n]=r%1e7,r=u(r/1e7)},y=function(t){for(var e=6,n=0;--e>=0;)n+=p[e],p[e]=u(n/t),n=n%t*1e7},d=function(){for(var t=6,e="";--t>=0;)if(""!==e||0===t||0!==p[t]){var n=String(p[t]);e=""===e?n:e+a.call("0",7-n.length)+n}return e};if(f<0||f>20)throw RangeError("Incorrect fraction digits");if(s!=s)return"NaN";if(s<=-1e21||s>=1e21)return String(s);if(s<0&&(g="-",s=-s),s>1e-21)if(n=(e=function(t){for(var e=0,n=t;n>=4096;)e+=12,n/=4096;for(;n>=2;)e+=1,n/=2;return e}(s*l(2,69,1))-69)<0?s*l(2,-e,1):s/l(2,e,1),n*=4503599627370496,(e=52-e)>0){for(v(0,n),r=f;r>=7;)v(1e7,0),r-=7;for(v(l(10,r,1),0),r=e-1;r>=23;)y(1<<23),r-=23;y(1<<r),v(1,1),y(2),m=d()}else v(0,n),v(1<<-e,0),m=d()+a.call("0",f);return m=f>0?g+((c=m.length)<=f?"0."+a.call("0",f-c)+m:m.slice(0,c-f)+"."+m.slice(c-f)):g+m}})},15:function(t,e){t.exports=function(t){if(null==t)throw TypeError("Can't call method on "+t);return t}},16:function(t,e,n){var r=n(0),o=n(9),i=n(2),a=n(23),c=n(40),s=n(35),u=s.get,l=s.enforce,f=String(String).split("String");(t.exports=function(t,e,n,c){var s,u=!!c&&!!c.unsafe,p=!!c&&!!c.enumerable,g=!!c&&!!c.noTargetGet;"function"==typeof n&&("string"!=typeof e||i(n,"name")||o(n,"name",e),(s=l(n)).source||(s.source=f.join("string"==typeof e?e:""))),t!==r?(u?!g&&t[e]&&(p=!0):delete t[e],p?t[e]=n:o(t,e,n)):p?t[e]=n:a(e,n)})(Function.prototype,"toString",(function(){return"function"==typeof this&&u(this).source||c(this)}))},17:function(t,e){t.exports={}},171:function(t,e,n){var r=n(21);t.exports=function(t){if("number"!=typeof t&&"Number"!=r(t))throw TypeError("Incorrect invocation");return+t}},172:function(t,e,n){"use strict";var r=n(20),o=n(15);t.exports="".repeat||function(t){var e=String(o(this)),n="",i=r(t);if(i<0||i==1/0)throw RangeError("Wrong number of repetitions");for(;i>0;(i>>>=1)&&(e+=e))1&i&&(n+=e);return n}},19:function(t,e){t.exports=function(t,e){return{enumerable:!(1&t),configurable:!(2&t),writable:!(4&t),value:e}}},2:function(t,e){var n={}.hasOwnProperty;t.exports=function(t,e){return n.call(t,e)}},20:function(t,e){var n=Math.ceil,r=Math.floor;t.exports=function(t){return isNaN(t=+t)?0:(t>0?r:n)(t)}},21:function(t,e){var n={}.toString;t.exports=function(t){return n.call(t).slice(8,-1)}},22:function(t,e,n){var r=n(4);t.exports=function(t,e){if(!r(t))return t;var n,o;if(e&&"function"==typeof(n=t.toString)&&!r(o=n.call(t)))return o;if("function"==typeof(n=t.valueOf)&&!r(o=n.call(t)))return o;if(!e&&"function"==typeof(n=t.toString)&&!r(o=n.call(t)))return o;throw TypeError("Can't convert object to primitive value")}},23:function(t,e,n){var r=n(0),o=n(9);t.exports=function(t,e){try{o(r,t,e)}catch(n){r[t]=e}return e}},24:function(t,e,n){var r=n(0),o=n(23),i=r["__core-js_shared__"]||o("__core-js_shared__",{});t.exports=i},26:function(t,e,n){var r=n(60),o=n(0),i=function(t){return"function"==typeof t?t:void 0};t.exports=function(t,e){return arguments.length<2?i(r[t])||i(o[t]):r[t]&&r[t][e]||o[t]&&o[t][e]}},27:function(t,e,n){var r=n(3),o=n(55),i=n(19),a=n(10),c=n(22),s=n(2),u=n(42),l=Object.getOwnPropertyDescriptor;e.f=r?l:function(t,e){if(t=a(t),e=c(e,!0),u)try{return l(t,e)}catch(t){}if(s(t,e))return i(!o.f.call(t,e),t[e])}},28:function(t,e,n){var r=n(3),o=n(1),i=n(2),a=Object.defineProperty,c={},s=function(t){throw t};t.exports=function(t,e){if(i(c,t))return c[t];e||(e={});var n=[][t],u=!!i(e,"ACCESSORS")&&e.ACCESSORS,l=i(e,0)?e[0]:s,f=i(e,1)?e[1]:void 0;return c[t]=!!n&&!o((function(){if(u&&!r)return!0;var t={length:-1};u?a(t,1,{enumerable:!0,get:s}):t[1]=1,n.call(t,l,f)}))}},29:function(t,e){t.exports=["constructor","hasOwnProperty","isPrototypeOf","propertyIsEnumerable","toLocaleString","toString","valueOf"]},3:function(t,e,n){var r=n(1);t.exports=!r((function(){return 7!=Object.defineProperty({},1,{get:function(){return 7}})[1]}))},31:function(t,e,n){var r=n(15);t.exports=function(t){return Object(r(t))}},32:function(t,e,n){"use strict";var r=n(6),o=n(1),i=n(57),a=n(4),c=n(31),s=n(12),u=n(75),l=n(78),f=n(69),p=n(5),g=n(79),m=p("isConcatSpreadable"),v=g>=51||!o((function(){var t=[];return t[m]=!1,t.concat()[0]!==t})),y=f("concat"),d=function(t){if(!a(t))return!1;var e=t[m];return void 0!==e?!!e:i(t)};r({target:"Array",proto:!0,forced:!v||!y},{concat:function(t){var e,n,r,o,i,a=c(this),f=l(a,0),p=0;for(e=-1,r=arguments.length;e<r;e++)if(d(i=-1===e?a:arguments[e])){if(p+(o=s(i.length))>9007199254740991)throw TypeError("Maximum allowed index exceeded");for(n=0;n<o;n++,p++)n in i&&u(f,p,i[n])}else{if(p>=9007199254740991)throw TypeError("Maximum allowed index exceeded");u(f,p++,i)}return f.length=p,f}})},33:function(t,e,n){var r=n(36),o=n(34),i=r("keys");t.exports=function(t){return i[t]||(i[t]=o(t))}},34:function(t,e){var n=0,r=Math.random();t.exports=function(t){return"Symbol("+String(void 0===t?"":t)+")_"+(++n+r).toString(36)}},35:function(t,e,n){var r,o,i,a=n(67),c=n(0),s=n(4),u=n(9),l=n(2),f=n(24),p=n(33),g=n(17),m=c.WeakMap;if(a){var v=f.state||(f.state=new m),y=v.get,d=v.has,S=v.set;r=function(t,e){return e.facade=t,S.call(v,t,e),e},o=function(t){return y.call(v,t)||{}},i=function(t){return d.call(v,t)}}else{var h=p("state");g[h]=!0,r=function(t,e){return e.facade=t,u(t,h,e),e},o=function(t){return l(t,h)?t[h]:{}},i=function(t){return l(t,h)}}t.exports={set:r,get:o,has:i,enforce:function(t){return i(t)?o(t):r(t,{})},getterFor:function(t){return function(e){var n;if(!s(e)||(n=o(e)).type!==t)throw TypeError("Incompatible receiver, "+t+" required");return n}}}},36:function(t,e,n){var r=n(41),o=n(24);(t.exports=function(t,e){return o[t]||(o[t]=void 0!==e?e:{})})("versions",[]).push({version:"3.8.1",mode:r?"pure":"global",copyright:"© 2020 Denis Pushkarev (zloirock.ru)"})},37:function(t,e,n){var r=n(1);t.exports=!!Object.getOwnPropertySymbols&&!r((function(){return!String(Symbol())}))},39:function(t,e,n){var r=n(1),o=n(21),i="".split;t.exports=r((function(){return!Object("z").propertyIsEnumerable(0)}))?function(t){return"String"==o(t)?i.call(t,""):Object(t)}:Object},4:function(t,e){t.exports=function(t){return"object"==typeof t?null!==t:"function"==typeof t}},40:function(t,e,n){var r=n(24),o=Function.toString;"function"!=typeof r.inspectSource&&(r.inspectSource=function(t){return o.call(t)}),t.exports=r.inspectSource},41:function(t,e){t.exports=!1},42:function(t,e,n){var r=n(3),o=n(1),i=n(46);t.exports=!r&&!o((function(){return 7!=Object.defineProperty(i("div"),"a",{get:function(){return 7}}).a}))},44:function(t,e,n){var r=n(48),o=n(29).concat("length","prototype");e.f=Object.getOwnPropertyNames||function(t){return r(t,o)}},46:function(t,e,n){var r=n(0),o=n(4),i=r.document,a=o(i)&&o(i.createElement);t.exports=function(t){return a?i.createElement(t):{}}},48:function(t,e,n){var r=n(2),o=n(10),i=n(51).indexOf,a=n(17);t.exports=function(t,e){var n,c=o(t),s=0,u=[];for(n in c)!r(a,n)&&r(c,n)&&u.push(n);for(;e.length>s;)r(c,n=e[s++])&&(~i(u,n)||u.push(n));return u}},49:function(t,e){function n(e){return"function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?t.exports=n=function(t){return typeof t}:t.exports=n=function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},n(e)}t.exports=n},5:function(t,e,n){var r=n(0),o=n(36),i=n(2),a=n(34),c=n(37),s=n(61),u=o("wks"),l=r.Symbol,f=s?l:l&&l.withoutSetter||a;t.exports=function(t){return i(u,t)||(c&&i(l,t)?u[t]=l[t]:u[t]=f("Symbol."+t)),u[t]}},50:function(t,e,n){var r=n(20),o=Math.max,i=Math.min;t.exports=function(t,e){var n=r(t);return n<0?o(n+e,0):i(n,e)}},51:function(t,e,n){var r=n(10),o=n(12),i=n(50),a=function(t){return function(e,n,a){var c,s=r(e),u=o(s.length),l=i(a,u);if(t&&n!=n){for(;u>l;)if((c=s[l++])!=c)return!0}else for(;u>l;l++)if((t||l in s)&&s[l]===n)return t||l||0;return!t&&-1}};t.exports={includes:a(!0),indexOf:a(!1)}},53:function(t,e,n){var r=n(1),o=/#|\.prototype\./,i=function(t,e){var n=c[a(t)];return n==u||n!=s&&("function"==typeof e?r(e):!!e)},a=i.normalize=function(t){return String(t).replace(o,".").toLowerCase()},c=i.data={},s=i.NATIVE="N",u=i.POLYFILL="P";t.exports=i},54:function(t,e,n){var r,o=n(7),i=n(83),a=n(29),c=n(17),s=n(81),u=n(46),l=n(33),f=l("IE_PROTO"),p=function(){},g=function(t){return"<script>"+t+"<\/script>"},m=function(){try{r=document.domain&&new ActiveXObject("htmlfile")}catch(t){}var t,e;m=r?function(t){t.write(g("")),t.close();var e=t.parentWindow.Object;return t=null,e}(r):((e=u("iframe")).style.display="none",s.appendChild(e),e.src=String("javascript:"),(t=e.contentWindow.document).open(),t.write(g("document.F=Object")),t.close(),t.F);for(var n=a.length;n--;)delete m.prototype[a[n]];return m()};c[f]=!0,t.exports=Object.create||function(t,e){var n;return null!==t?(p.prototype=o(t),n=new p,p.prototype=null,n[f]=t):n=m(),void 0===e?n:i(n,e)}},55:function(t,e,n){"use strict";var r={}.propertyIsEnumerable,o=Object.getOwnPropertyDescriptor,i=o&&!r.call({1:2},1);e.f=i?function(t){var e=o(this,t);return!!e&&e.enumerable}:r},559:function(t,e,n){t.exports=n(560)},56:function(t,e){e.f=Object.getOwnPropertySymbols},560:function(t,e,n){n(32),n(85),n(74),n(146),n(66),n(86),n(32),n(85),n(74),n(146),n(66),n(86),function(t){t.fn.tkVectorWorldMapGDP=function(){if(this.length){var t=window.jVectorMapGdpData;void 0!==t&&this.vectorMap({map:"world_mill_en",zoomOnScroll:!1,backgroundColor:"#fff",series:{regions:[{values:t,scale:[settings.colors.primary[500],settings.colors.success[500]],normalizeFunction:"polynomial"}]},onLabelShow:function(e,n,r){n.html(n.html()+" (GDP - "+t[r]+")")}})}},t.fn.tkVectorWorldMapMarkers=function(){this.length&&this.vectorMap({map:"world_mill_en",regionStyle:{initial:{fill:settings.colors.gray[300]}},zoomOnScroll:!1,normalizeFunction:"polynomial",hoverOpacity:.7,hoverColor:!1,markerStyle:{initial:{fill:settings.colors.primary[500],stroke:"#fff"}},backgroundColor:"#fff",markers:[{latLng:[41.9,12.45],name:"Vatican City"},{latLng:[43.73,7.41],name:"Monaco"},{latLng:[-.52,166.93],name:"Nauru"},{latLng:[-8.51,179.21],name:"Tuvalu"},{latLng:[43.93,12.46],name:"San Marino"},{latLng:[47.14,9.52],name:"Liechtenstein"},{latLng:[7.11,171.06],name:"Marshall Islands"},{latLng:[17.3,-62.73],name:"Saint Kitts and Nevis"},{latLng:[3.2,73.22],name:"Maldives"},{latLng:[35.88,14.5],name:"Malta"},{latLng:[12.05,-61.75],name:"Grenada"},{latLng:[13.16,-61.23],name:"Saint Vincent and the Grenadines"},{latLng:[13.16,-59.55],name:"Barbados"},{latLng:[17.11,-61.85],name:"Antigua and Barbuda"},{latLng:[-4.61,55.45],name:"Seychelles"},{latLng:[7.35,134.46],name:"Palau"},{latLng:[42.5,1.51],name:"Andorra"},{latLng:[14.01,-60.98],name:"Saint Lucia"},{latLng:[6.91,158.18],name:"Federated States of Micronesia"},{latLng:[1.3,103.8],name:"Singapore"},{latLng:[1.46,173.03],name:"Kiribati"},{latLng:[-21.13,-175.2],name:"Tonga"},{latLng:[15.3,-61.38],name:"Dominica"},{latLng:[-20.2,57.5],name:"Mauritius"},{latLng:[26.02,50.55],name:"Bahrain"},{latLng:[.33,6.73],name:"So Tom and Prncipe"}]})},t.fn.tkVectorUSAUnemployment=function(){if(this.length){var e=this;t.getJSON("assets/data/vector-maps/data/us-unemployment.json",(function(t){var n=jvm.values.apply({},jvm.values(t.states)),r=Array.prototype.concat.apply([],jvm.values(t.metro.population)),o=Array.prototype.concat.apply([],jvm.values(t.metro.unemployment));e.vectorMap({map:"us_aea_en",markers:t.metro.coords,backgroundColor:"#fff",zoomOnScroll:!1,series:{markers:[{attribute:"fill",scale:[settings.colors.primary[300]],values:t.metro.unemployment[2009],min:jvm.min(o),max:jvm.max(o)},{attribute:"r",scale:[5,20],values:t.metro.population[2009],min:jvm.min(r),max:jvm.max(r)}],regions:[{scale:[settings.colors.primary[500],settings.colors.success[500]],attribute:"fill",values:t.states[2009],min:jvm.min(n),max:jvm.max(n)}]},onMarkerLabelShow:function(e,n,r){n.html("<b>"+t.metro.names[r]+"</b><br/><b>Population: </b>"+t.metro.population[2009][r]+"</br><b>Unemployment rate: </b>"+t.metro.unemployment[2009][r]+"%")},onRegionLabelShow:function(e,n,r){n.html("<b>"+n.html()+"</b></br><b>Unemployment rate: </b>"+t.states[2009][r]+"%")}})}))}},t.fn.tkVectorRegionSelection=function(){if(this.length){var t=new jvm.Map({container:this,map:"de_merc_en",regionsSelectable:!0,markersSelectable:!0,backgroundColor:"#fff",zoomOnScroll:!1,markers:[{latLng:[52.5,13.39],name:"Berlin"},{latLng:[53.56,10],name:"Hamburg"},{latLng:[48.13,11.56],name:"Munich"},{latLng:[50.95,6.96],name:"Cologne"},{latLng:[50.11,8.68],name:"Frankfurt am Main"},{latLng:[48.77,9.17],name:"Stuttgart"},{latLng:[51.23,6.78],name:"Dusseldorf"},{latLng:[51.51,7.46],name:"Dortmund"},{latLng:[51.45,7.01],name:"Essen"},{latLng:[53.07,8.8],name:"Bremen"}],markerStyle:{initial:{fill:settings.colors.primary[300]},selected:{fill:settings.colors.success[500]}},regionStyle:{initial:{fill:settings.colors.primary[500]},selected:{fill:settings.colors.gray[700]}},series:{markers:[{attribute:"r",scale:[5,15],values:[887.7,755.16,310.69,405.17,248.31,207.35,217.22,280.71,210.32,325.42]}]},onRegionSelected:function(){window.localStorage&&window.localStorage.setItem("jvectormap-selected-regions",JSON.stringify(t.getSelectedRegions()))},onMarkerSelected:function(){window.localStorage&&window.localStorage.setItem("jvectormap-selected-markers",JSON.stringify(t.getSelectedMarkers()))}});t.setSelectedRegions(JSON.parse(window.localStorage.getItem("jvectormap-selected-regions")||"[]")),t.setSelectedMarkers(JSON.parse(window.localStorage.getItem("jvectormap-selected-markers")||"[]"))}},t.fn.tkVectorFranceElections=function(){this.length&&t.getJSON("assets/data/vector-maps/data/france-elections.json",(function(e){new jvm.Map({map:"fr_merc_en",backgroundColor:"#fff",container:t("#france-2007"),zoomOnScroll:!1,series:{regions:[{scale:{1:settings.colors.primary[500],2:settings.colors.primary[300]},attribute:"fill",values:e.year2007.results}]}}),new jvm.Map({map:"fr_merc_en",container:t("#france-2012"),backgroundColor:"#fff",zoomOnScroll:!1,series:{regions:[{scale:{1:settings.colors.primary[500],2:settings.colors.primary[300]},attribute:"fill",values:e.year2012.results}]}})}))};var e,n=[settings.colors.primary[300],settings.colors.primary[500],settings.colors.success[500],settings.colors.gray[300],settings.colors.success[500],settings.colors.success[600]],r=function(){var t,r={};for(t in e.regions)r[t]=n[Math.floor(Math.random()*n.length)];return r};t.fn.tkVectorRandomColors=function(){this.length&&((e=new jvm.Map({map:"es_merc_en",backgroundColor:"#fff",container:this,zoomOnScroll:!1,series:{regions:[{attribute:"fill"}]}})).series.regions[0].setValues(r()),t("#update-colors-button").click((function(t){t.preventDefault(),e.series.regions[0].setValues(r())})))},t.fn.tkVectorMallMap=function(){this.length&&this.vectorMap({map:"mall",backgroundColor:"#fff",zoomOnScroll:!1,markers:[{coords:[60,110],name:"Escalator 1",style:{fill:settings.colors.primary[300],stroke:"#fff"}},{coords:[260,95],name:"Escalator 2",style:{fill:settings.colors.primary[300],stroke:"#fff"}},{coords:[434,95],name:"Escalator 3",style:{fill:settings.colors.primary[300],stroke:"#fff"}},{coords:[634,110],name:"Escalator 4",style:{fill:settings.colors.primary[300],stroke:"#fff"}}],series:{regions:[{values:{F102:"SPORTS & OUTDOOR",F103:"HOME DECOR",F105:"FASHION",F106:"OTHER",F108:"BEAUTY & SPA",F109:"FASHION",F110:"BEAUTY & SPA",F111:"URBAN FAVORITES",F114:"SERVICES",F166:"DINING",F167:"FASHION",F169:"DINING",F170:"ENTERTAINMENT",F172:"DINING",F174:"DINING",F115:"KIDS STUFF",F117:"LIFESTYLE",F118:"URBAN FAVORITES",F119:"FASHION",F120:"FASHION",F122:"KIDS STUFF",F124:"KIDS STUFF",F125:"KIDS STUFF",F126:"KIDS STUFF",F128:"KIDS STUFF",F129:"LIFESTYLE",F130:"HOME DECOR",F132:"DINING",F133:"SPORTS & OUTDOOR",F134:"KIDS STUFF",F135:"LIFESTYLE",F136:"LIFESTYLE",F139:"KIDS STUFF",F153:"DINING",F155:"FASHION",F156:"URBAN FAVORITES",F157:"URBAN FAVORITES",F158:"LINGERIE & UNDERWEAR",F159:"FASHION",F160:"FASHION",F162:"FASHION",F164:"FASHION",F165:"FASHION",FR01:"REST ROOMS",FR02:"REST ROOMS",FR03:"REST ROOMS",FR04:"REST ROOMS",FFC:"DINING"},scale:{FASHION:"#2761ad","LINGERIE & UNDERWEAR":"#d58aa3","BEAUTY & SPA":settings.colors.success[500],"URBAN FAVORITES":settings.colors.primary[900],"SPORTS & OUTDOOR":settings.colors.success[500],"KIDS STUFF":settings.colors.success[300],ENTERTAINMENT:settings.colors.success[500],"HOME DECOR":settings.colors.gray[400],LIFESTYLE:settings.colors.gray[300],DINING:settings.colors.success[500],"REST ROOMS":settings.colors.gray[700],SERVICES:settings.colors.gray[300],OTHER:settings.colors.gray[500]}}]},onRegionLabelShow:function(t,e,n){""===e.html()&&t.preventDefault()}})},t.fn.tkVectorProjectionMap=function(){if(this.length){var e,n=0,r={};(e=new jvm.Map({map:"us_lcc_en",zoomOnScroll:!1,regionStyle:{initial:{fill:settings.colors.primary[500]}},backgroundColor:"#fff",markerStyle:{initial:{fill:"red"}},container:this,onMarkerLabelShow:function(t,n,o){e.label.text(r[o].lat.toFixed(2)+", "+r[o].lng.toFixed(2))},onMarkerClick:function(t,n){e.removeMarkers([n]),e.label.hide()}})).container.click((function(o){var i=e.pointToLatLng(o.offsetX,o.offsetY),a=t(o.target).attr("class");i&&(!a||a&&-1===t(o.target).attr("class").indexOf("jvectormap-marker"))&&(r[n]=i,e.addMarker(n,{latLng:[i.lat,i.lng]}),n+=1)}))}},t('[data-toggle="vector-world-map-gdp"]').tkVectorWorldMapGDP(),t('[data-toggle="vector-world-map-markers"]').tkVectorWorldMapMarkers(),t('[data-toggle="vector-usa-unemployment"]').tkVectorUSAUnemployment(),t('[data-toggle="vector-region-selection"]').tkVectorRegionSelection(),t('[data-toggle="vector-france-elections"]').tkVectorFranceElections(),t('[data-toggle="vector-random-colors"]').tkVectorRandomColors(),t('[data-toggle="vector-mall-map"]').tkVectorMallMap(),t('[data-toggle="vector-projection-map"]').tkVectorProjectionMap()}(jQuery)},57:function(t,e,n){var r=n(21);t.exports=Array.isArray||function(t){return"Array"==r(t)}},58:function(t,e,n){var r,o=n(49);r=function(){return this}();try{r=r||new Function("return this")()}catch(t){"object"===("undefined"==typeof window?"undefined":o(window))&&(r=window)}t.exports=r},59:function(t,e,n){var r=n(2),o=n(65),i=n(27),a=n(8);t.exports=function(t,e){for(var n=o(e),c=a.f,s=i.f,u=0;u<n.length;u++){var l=n[u];r(t,l)||c(t,l,s(e,l))}}},6:function(t,e,n){var r=n(0),o=n(27).f,i=n(9),a=n(16),c=n(23),s=n(59),u=n(53);t.exports=function(t,e){var n,l,f,p,g,m=t.target,v=t.global,y=t.stat;if(n=v?r:y?r[m]||c(m,{}):(r[m]||{}).prototype)for(l in e){if(p=e[l],f=t.noTargetGet?(g=o(n,l))&&g.value:n[l],!u(v?l:m+(y?".":"#")+l,t.forced)&&void 0!==f){if(typeof p==typeof f)continue;s(p,f)}(t.sham||f&&f.sham)&&i(p,"sham",!0),a(n,l,p,t)}}},60:function(t,e,n){var r=n(0);t.exports=r},61:function(t,e,n){var r=n(37);t.exports=r&&!Symbol.sham&&"symbol"==typeof Symbol.iterator},62:function(t,e,n){var r=n(48),o=n(29);t.exports=Object.keys||function(t){return r(t,o)}},65:function(t,e,n){var r=n(26),o=n(44),i=n(56),a=n(7);t.exports=r("Reflect","ownKeys")||function(t){var e=o.f(a(t)),n=i.f;return n?e.concat(n(t)):e}},66:function(t,e,n){var r=n(87),o=n(16),i=n(116);r||o(Object.prototype,"toString",i,{unsafe:!0})},67:function(t,e,n){var r=n(0),o=n(40),i=r.WeakMap;t.exports="function"==typeof i&&/native code/.test(o(i))},69:function(t,e,n){var r=n(1),o=n(5),i=n(79),a=o("species");t.exports=function(t){return i>=51||!r((function(){var e=[];return(e.constructor={})[a]=function(){return{foo:1}},1!==e[t](Boolean).foo}))}},7:function(t,e,n){var r=n(4);t.exports=function(t){if(!r(t))throw TypeError(String(t)+" is not an object");return t}},70:function(t,e){t.exports={}},71:function(t,e,n){var r=n(5),o=n(54),i=n(8),a=r("unscopables"),c=Array.prototype;null==c[a]&&i.f(c,a,{configurable:!0,value:o(null)}),t.exports=function(t){c[a][t]=!0}},74:function(t,e,n){"use strict";var r=n(10),o=n(71),i=n(70),a=n(35),c=n(99),s=a.set,u=a.getterFor("Array Iterator");t.exports=c(Array,"Array",(function(t,e){s(this,{type:"Array Iterator",target:r(t),index:0,kind:e})}),(function(){var t=u(this),e=t.target,n=t.kind,r=t.index++;return!e||r>=e.length?(t.target=void 0,{value:void 0,done:!0}):"keys"==n?{value:r,done:!1}:"values"==n?{value:e[r],done:!1}:{value:[r,e[r]],done:!1}}),"values"),i.Arguments=i.Array,o("keys"),o("values"),o("entries")},75:function(t,e,n){"use strict";var r=n(22),o=n(8),i=n(19);t.exports=function(t,e,n){var a=r(e);a in t?o.f(t,a,i(0,n)):t[a]=n}},78:function(t,e,n){var r=n(4),o=n(57),i=n(5)("species");t.exports=function(t,e){var n;return o(t)&&("function"!=typeof(n=t.constructor)||n!==Array&&!o(n.prototype)?r(n)&&null===(n=n[i])&&(n=void 0):n=void 0),new(void 0===n?Array:n)(0===e?0:e)}},79:function(t,e,n){var r,o,i=n(0),a=n(95),c=i.process,s=c&&c.versions,u=s&&s.v8;u?o=(r=u.split("."))[0]+r[1]:a&&(!(r=a.match(/Edge\/(\d+)/))||r[1]>=74)&&(r=a.match(/Chrome\/(\d+)/))&&(o=r[1]),t.exports=o&&+o},8:function(t,e,n){var r=n(3),o=n(42),i=n(7),a=n(22),c=Object.defineProperty;e.f=r?c:function(t,e,n){if(i(t),e=a(e,!0),i(n),o)try{return c(t,e,n)}catch(t){}if("get"in n||"set"in n)throw TypeError("Accessors not supported");return"value"in n&&(t[e]=n.value),t}},80:function(t,e,n){var r=n(8).f,o=n(2),i=n(5)("toStringTag");t.exports=function(t,e,n){t&&!o(t=n?t:t.prototype,i)&&r(t,i,{configurable:!0,value:e})}},81:function(t,e,n){var r=n(26);t.exports=r("document","documentElement")},83:function(t,e,n){var r=n(3),o=n(8),i=n(7),a=n(62);t.exports=r?Object.defineProperties:function(t,e){i(t);for(var n,r=a(e),c=r.length,s=0;c>s;)o.f(t,n=r[s++],e[n]);return t}},84:function(t,e,n){"use strict";var r=n(1);t.exports=function(t,e){var n=[][t];return!!n&&r((function(){n.call(null,e||function(){throw 1},1)}))}},85:function(t,e,n){"use strict";var r=n(6),o=n(51).indexOf,i=n(84),a=n(28),c=[].indexOf,s=!!c&&1/[1].indexOf(1,-0)<0,u=i("indexOf"),l=a("indexOf",{ACCESSORS:!0,1:0});r({target:"Array",proto:!0,forced:s||!u||!l},{indexOf:function(t){return s?c.apply(this,arguments)||0:o(this,t,arguments.length>1?arguments[1]:void 0)}})},86:function(t,e,n){var r=n(0),o=n(94),i=n(74),a=n(9),c=n(5),s=c("iterator"),u=c("toStringTag"),l=i.values;for(var f in o){var p=r[f],g=p&&p.prototype;if(g){if(g[s]!==l)try{a(g,s,l)}catch(t){g[s]=l}if(g[u]||a(g,u,f),o[f])for(var m in i)if(g[m]!==i[m])try{a(g,m,i[m])}catch(t){g[m]=i[m]}}}},87:function(t,e,n){var r={};r[n(5)("toStringTag")]="z",t.exports="[object z]"===String(r)},9:function(t,e,n){var r=n(3),o=n(8),i=n(19);t.exports=r?function(t,e,n){return o.f(t,e,i(1,n))}:function(t,e,n){return t[e]=n,t}},94:function(t,e){t.exports={CSSRuleList:0,CSSStyleDeclaration:0,CSSValueList:0,ClientRectList:0,DOMRectList:0,DOMStringList:0,DOMTokenList:1,DataTransferItemList:0,FileList:0,HTMLAllCollection:0,HTMLCollection:0,HTMLFormElement:0,HTMLSelectElement:0,MediaList:0,MimeTypeArray:0,NamedNodeMap:0,NodeList:1,PaintRequestList:0,Plugin:0,PluginArray:0,SVGLengthList:0,SVGNumberList:0,SVGPathSegList:0,SVGPointList:0,SVGStringList:0,SVGTransformList:0,SourceBufferList:0,StyleSheetList:0,TextTrackCueList:0,TextTrackList:0,TouchList:0}},95:function(t,e,n){var r=n(26);t.exports=r("navigator","userAgent")||""},97:function(t,e,n){var r=n(2),o=n(31),i=n(33),a=n(112),c=i("IE_PROTO"),s=Object.prototype;t.exports=a?Object.getPrototypeOf:function(t){return t=o(t),r(t,c)?t[c]:"function"==typeof t.constructor&&t instanceof t.constructor?t.constructor.prototype:t instanceof Object?s:null}},99:function(t,e,n){"use strict";var r=n(6),o=n(122),i=n(97),a=n(106),c=n(80),s=n(9),u=n(16),l=n(5),f=n(41),p=n(70),g=n(103),m=g.IteratorPrototype,v=g.BUGGY_SAFARI_ITERATORS,y=l("iterator"),d=function(){return this};t.exports=function(t,e,n,l,g,S,h){o(n,e,l);var b,O,x,F=function(t){if(t===g&&w)return w;if(!v&&t in T)return T[t];switch(t){case"keys":case"values":case"entries":return function(){return new n(this,t)}}return function(){return new n(this)}},L=e+" Iterator",E=!1,T=t.prototype,I=T[y]||T["@@iterator"]||g&&T[g],w=!v&&I||F(g),j="Array"==e&&T.entries||I;if(j&&(b=i(j.call(new t)),m!==Object.prototype&&b.next&&(f||i(b)===m||(a?a(b,m):"function"!=typeof b[y]&&s(b,y,d)),c(b,L,!0,!0),f&&(p[L]=d))),"values"==g&&I&&"values"!==I.name&&(E=!0,w=function(){return I.call(this)}),f&&!h||T[y]===w||s(T,y,w),p[e]=w,g)if(O={values:F("values"),keys:S?w:F("keys"),entries:F("entries")},h)for(x in O)(v||E||!(x in T))&&u(T,x,O[x]);else r({target:e,proto:!0,forced:v||E},O);return O}}});