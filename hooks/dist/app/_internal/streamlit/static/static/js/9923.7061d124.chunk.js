"use strict";(self.webpackChunk_streamlit_app=self.webpackChunk_streamlit_app||[]).push([[9923],{19923:(e,t,n)=>{n.r(t),n.d(t,{default:()=>c});n(58878);var i=n(22044),o=n(89653);const s=(0,o.A)("div",{target:"e115fcil2"})((e=>{let{theme:t}=e;return{display:"flex",flexDirection:"row",flexWrap:"wrap",rowGap:t.spacing.lg}}),""),r=(0,o.A)("div",{target:"e115fcil1"})((()=>({display:"flex",flexDirection:"column",alignItems:"stretch",width:"auto",flexGrow:0})),""),l=(0,o.A)("div",{target:"e115fcil0"})((e=>{let{theme:t}=e;return{fontFamily:t.genericFonts.bodyFont,fontSize:t.fontSizes.sm,color:t.colors.fadedText60,textAlign:"center",marginTop:t.spacing.xs,wordWrap:"break-word",padding:t.spacing.threeXS}}),"");var d,a=n(90782);!function(e){e[e.OriginalWidth=-1]="OriginalWidth",e[e.ColumnWidth=-2]="ColumnWidth",e[e.AutoWidth=-3]="AutoWidth"}(d||(d={}));const c=(0,i.A)((function(e){let t,{width:n,isFullScreen:i,element:o,height:c,endpoints:h}=e;const u=o.width;if(u===d.OriginalWidth||u===d.AutoWidth)t=void 0;else if(u===d.ColumnWidth)t=n;else{if(!(u>0))throw Error(`Invalid image width: ${u}`);t=u}const m={};return c&&i?(m.maxHeight=c,m.objectFit="contain"):(m.width=t,u===d.AutoWidth&&(m.maxWidth="100%")),(0,a.jsx)(s,{className:"stImage","data-testid":"stImage",style:{width:n},children:o.imgs.map(((e,t)=>{const n=e;return(0,a.jsxs)(r,{"data-testid":"stImageContainer",children:[(0,a.jsx)("img",{style:m,src:h.buildMediaURL(n.url),alt:t.toString()}),n.caption&&(0,a.jsx)(l,{"data-testid":"stImageCaption",style:m,children:` ${n.caption} `})]},t)}))})}))},22044:(e,t,n)=>{n.d(t,{A:()=>w});var i=n(58878),o=n(53124),s=n.n(o),r=n(8151),l=n(41514),d=n(67214),a=n(64611),c=n(84152),h=n(89653);const u=(0,h.A)("button",{target:"e1vs0wn31"})((e=>{let{isExpanded:t,theme:n}=e;const i=t?{right:"0.4rem",top:"0.5rem",backgroundColor:"transparent"}:{right:"-3.0rem",top:"-0.375rem",opacity:0,transform:"scale(0)",backgroundColor:n.colors.lightenedBg05};return{position:"absolute",display:"flex",alignItems:"center",justifyContent:"center",zIndex:n.zIndices.sidebar+1,height:"2.5rem",width:"2.5rem",transition:"opacity 300ms 150ms, transform 300ms 150ms",border:"none",color:n.colors.fadedText60,borderRadius:"50%",...i,"&:focus":{outline:"none"},"&:active, &:focus-visible, &:hover":{opacity:1,outline:"none",transform:"scale(1)",color:n.colors.bodyText,transition:"none"}}}),""),m=(0,h.A)("div",{target:"e1vs0wn30"})((e=>{let{theme:t,isExpanded:n}=e;return{"&:hover":{[u]:{opacity:1,transform:"scale(1)",transition:"none"}},...n?{position:"fixed",top:0,left:0,bottom:0,right:0,background:t.colors.bgColor,zIndex:t.zIndices.fullscreenWrapper,padding:t.spacing.md,paddingTop:t.sizes.fullScreenHeaderHeight,overflow:["auto","overlay"],display:"flex",alignItems:"center",justifyContent:"center"}:{}}}),"");var p=n(90782);class g extends i.PureComponent{constructor(e){super(e),this.context=void 0,this.controlKeys=e=>{const{expanded:t}=this.state;27===e.keyCode&&t&&this.zoomOut()},this.zoomIn=()=>{document.body.style.overflow="hidden",this.context.setFullScreen(!0),this.setState({expanded:!0})},this.zoomOut=()=>{document.body.style.overflow="unset",this.context.setFullScreen(!1),this.setState({expanded:!1})},this.convertScssRemValueToPixels=e=>parseFloat(e)*parseFloat(getComputedStyle(document.documentElement).fontSize),this.getWindowDimensions=()=>{const e=this.convertScssRemValueToPixels(this.props.theme.spacing.md),t=this.convertScssRemValueToPixels(this.props.theme.sizes.fullScreenHeaderHeight);return{fullWidth:window.innerWidth-2*e,fullHeight:window.innerHeight-(e+t)}},this.updateWindowDimensions=()=>{this.setState(this.getWindowDimensions())},this.state={expanded:!1,...this.getWindowDimensions()}}componentDidMount(){window.addEventListener("resize",this.updateWindowDimensions),document.addEventListener("keydown",this.controlKeys,!1)}componentWillUnmount(){window.removeEventListener("resize",this.updateWindowDimensions),document.removeEventListener("keydown",this.controlKeys,!1)}render(){const{expanded:e,fullWidth:t,fullHeight:n}=this.state,{children:i,width:o,height:s,disableFullscreenMode:r}=this.props;let c=l.u,h=this.zoomIn,g="View fullscreen";return e&&(c=d.Q,h=this.zoomOut,g="Exit fullscreen"),(0,p.jsxs)(m,{isExpanded:e,"data-testid":"stFullScreenFrame",children:[!r&&(0,p.jsx)(u,{"data-testid":"StyledFullScreenButton",onClick:h,title:g,isExpanded:e,children:(0,p.jsx)(a.A,{content:c})}),i(e?{width:t,height:n,expanded:e,expand:this.zoomIn,collapse:this.zoomOut}:{width:o,height:s,expanded:e,expand:this.zoomIn,collapse:this.zoomOut})]})}}g.contextType=c.n;const f=(0,r.b)(g);const w=function(e){let t=arguments.length>1&&void 0!==arguments[1]&&arguments[1];class n extends i.PureComponent{constructor(){super(...arguments),this.render=()=>{const{width:n,height:i,disableFullscreenMode:o}=this.props;return(0,p.jsx)(f,{width:n,height:i,disableFullscreenMode:t||o,children:t=>{let{width:n,height:i,expanded:o,expand:s,collapse:r}=t;return(0,p.jsx)(e,{...this.props,width:n,height:i,isFullScreen:o,expand:s,collapse:r})}})}}}return n.displayName=`withFullScreenWrapper(${e.displayName||e.name})`,s()(n,e)}},41514:(e,t,n)=>{n.d(t,{u:()=>r});var i=n(68102),o=n(58878),s=n(68622),r=o.forwardRef((function(e,t){return o.createElement(s.I,(0,i.A)({iconAttrs:{fill:"currentColor",xmlns:"http://www.w3.org/2000/svg"},iconVerticalAlign:"middle",iconViewBox:"0 0 8 8"},e,{ref:t}),o.createElement("path",{d:"M0 0v4l1.5-1.5L3 4l1-1-1.5-1.5L4 0H0zm5 4L4 5l1.5 1.5L4 8h4V4L6.5 5.5 5 4z"}))}));r.displayName="FullscreenEnter"},67214:(e,t,n)=>{n.d(t,{Q:()=>r});var i=n(68102),o=n(58878),s=n(68622),r=o.forwardRef((function(e,t){return o.createElement(s.I,(0,i.A)({iconAttrs:{fill:"currentColor",xmlns:"http://www.w3.org/2000/svg"},iconVerticalAlign:"middle",iconViewBox:"0 0 8 8"},e,{ref:t}),o.createElement("path",{d:"M1 0L0 1l1.5 1.5L0 4h4V0L2.5 1.5 1 0zm3 4v4l1.5-1.5L7 8l1-1-1.5-1.5L8 4H4z"}))}));r.displayName="FullscreenExit"}}]);