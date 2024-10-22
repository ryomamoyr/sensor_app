"use strict";(self.webpackChunk_streamlit_app=self.webpackChunk_streamlit_app||[]).push([[8815],{34752:(e,t,s)=>{s.d(t,{X:()=>n,o:()=>r});var i=s(58878),o=s(25571);class r{constructor(){this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}manageFormClearListener(e,t,s){(0,o.se)(this.formClearListener)&&this.lastWidgetMgr===e&&this.lastFormId===t||(this.disconnect(),(0,o._L)(t)&&(this.formClearListener=e.addFormClearedListener(t,s),this.lastWidgetMgr=e,this.lastFormId=t))}disconnect(){var e;null===(e=this.formClearListener)||void 0===e||e.disconnect(),this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}}function n(e){let{element:t,widgetMgr:s,onFormCleared:r}=e;(0,i.useEffect)((()=>{if(!(0,o._L)(t.formId))return;const e=s.addFormClearedListener(t.formId,r);return()=>{e.disconnect()}}),[t,s,r])}},48815:(e,t,s)=>{s.r(t),s.d(t,{default:()=>x});var i=s(58878),o=s(2273),r=s(64506),n=s.n(r),l=s(8151),a=s(3680),d=s(4314),h=s(80956),p=s(34752),c=s(70474),m=s(78286);const u=(0,s(89653).A)("div",{target:"e6zijwc0"})((e=>{let{theme:t}=e;return{"span[aria-disabled='true']":{background:t.colors.fadedText05}}}),"");var g=s(93480),v=s(997),f=s(43652),b=s(4871),y=s(25571),S=s(90782);class C extends i.PureComponent{constructor(){super(...arguments),this.formClearHelper=new p.o,this.state={value:this.initialValue},this.commitWidgetValue=e=>{const{widgetMgr:t,element:s,fragmentId:i}=this.props;t.setIntArrayValue(s,this.state.value,e,i)},this.onFormCleared=()=>{this.setState(((e,t)=>({value:t.element.default})),(()=>this.commitWidgetValue({fromUi:!0})))},this.onChange=e=>{this.props.element.maxSelections&&"select"===e.type&&this.state.value.length>=this.props.element.maxSelections||this.setState(this.generateNewState(e),(()=>{this.commitWidgetValue({fromUi:!0})}))},this.filterOptions=(e,t)=>{if(this.overMaxSelections())return[];const s=e.filter((e=>!this.state.value.includes(Number(e.value))));return(0,b.VC)(s,t)}}overMaxSelections(){return this.props.element.maxSelections>0&&this.state.value.length>=this.props.element.maxSelections}getNoResultsMsg(){const{maxSelections:e}=this.props.element,{value:t}=this.state;if(0===e)return"No results";if(t.length===e){return`You can only select up to ${e} ${1!==e?"options":"option"}. Remove an option first.`}return"No results"}get initialValue(){const e=this.props.widgetMgr.getIntArrayValue(this.props.element);return void 0!==e?e:this.props.element.default}componentDidMount(){this.props.element.setValue?this.updateFromProtobuf():this.commitWidgetValue({fromUi:!1})}componentDidUpdate(){this.maybeUpdateFromProtobuf()}componentWillUnmount(){this.formClearHelper.disconnect()}maybeUpdateFromProtobuf(){const{setValue:e}=this.props.element;e&&this.updateFromProtobuf()}updateFromProtobuf(){const{value:e}=this.props.element;this.props.element.setValue=!1,this.setState({value:e},(()=>{this.commitWidgetValue({fromUi:!1})}))}get valueFromState(){return this.state.value.map((e=>{const t=this.props.element.options[e];return{value:e.toString(),label:t}}))}generateNewState(e){const t=()=>{var t;const s=null===(t=e.option)||void 0===t?void 0:t.value;return parseInt(s,10)};switch(e.type){case"remove":return{value:n()(this.state.value,t())};case"clear":return{value:[]};case"select":return{value:this.state.value.concat([t()])};default:throw new Error(`State transition is unknown: ${e.type}`)}}render(){var e;const{element:t,theme:s,width:i,widgetMgr:r}=this.props,n={width:i},{options:l}=t,p=0===l.length||this.props.disabled,b=0===l.length?"No options to select.":t.placeholder,C=l.map(((e,t)=>({label:e,value:t.toString()})));this.formClearHelper.manageFormClearListener(r,t.formId,this.onFormCleared);const x=l.length>10;return(0,S.jsxs)("div",{className:"stMultiSelect","data-testid":"stMultiSelect",style:n,children:[(0,S.jsx)(c.L,{label:t.label,disabled:p,labelVisibility:(0,y.yv)(null===(e=t.labelVisibility)||void 0===e?void 0:e.value),children:t.help&&(0,S.jsx)(m.j,{children:(0,S.jsx)(g.A,{content:t.help,placement:v.W.TOP_RIGHT})})}),(0,S.jsx)(u,{children:(0,S.jsx)(d.A,{options:C,labelKey:"label",valueKey:"value","aria-label":t.label,placeholder:b,type:h.ZE.select,multi:!0,onChange:this.onChange,value:this.valueFromState,disabled:p,size:"compact",noResultsMsg:this.getNoResultsMsg(),filterOptions:this.filterOptions,closeOnSelect:!1,overrides:{SelectArrow:{component:a.A,props:{overrides:{Svg:{style:()=>({width:s.iconSizes.xl,height:s.iconSizes.xl})}}}},IconsContainer:{style:()=>({paddingRight:s.spacing.sm})},ControlContainer:{style:{minHeight:s.sizes.minElementHeight,borderLeftWidth:s.sizes.borderWidth,borderRightWidth:s.sizes.borderWidth,borderTopWidth:s.sizes.borderWidth,borderBottomWidth:s.sizes.borderWidth}},Placeholder:{style:()=>({flex:"inherit",opacity:"0.7"})},ValueContainer:{style:()=>({paddingLeft:s.spacing.sm,paddingTop:s.spacing.none,paddingBottom:s.spacing.none,paddingRight:s.spacing.none})},ClearIcon:{props:{overrides:{Svg:{style:{color:s.colors.darkGray,transform:"scale(1.5)",width:s.spacing.twoXL,":hover":{fill:s.colors.bodyText}}}}}},SearchIcon:{style:{color:s.colors.darkGray}},Tag:{props:{overrides:{Root:{style:{borderTopLeftRadius:s.radii.md,borderTopRightRadius:s.radii.md,borderBottomRightRadius:s.radii.md,borderBottomLeftRadius:s.radii.md,fontSize:s.fontSizes.sm,paddingLeft:s.spacing.sm,marginLeft:s.spacing.none,marginRight:s.spacing.sm,height:"28px",maxWidth:`calc(100% - ${s.spacing.lg})`}},Action:{style:{paddingLeft:0}},ActionIcon:{props:{overrides:{Svg:{style:{width:"10px",height:"10px"}}}}},Text:{style:{fontSize:s.fontSizes.md}}}}},MultiValue:{props:{overrides:{Root:{style:{fontSize:s.fontSizes.sm}}}}},Input:{props:{readOnly:o.Fr&&!1===x?"readonly":null}},Dropdown:{component:f.A}}})})]})}}const x=(0,l.b)(C)}}]);