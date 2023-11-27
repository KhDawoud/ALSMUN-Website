<script lang="ts">
  import { Router, Route } from 'svelte-routing';
  import LoginForm from "./lib/Pages/LoginForm.svelte";
  import Home from './lib/Pages/Home.svelte';
  import AboutUs from './lib/Pages/AboutUs.svelte';
  import MeetTeam from './lib/Pages/Team Pages/MeetTeam.svelte';
  import Secretariat from './lib/Pages/Team Pages/Secretariat.svelte';
  import OC from './lib/Pages/Team Pages/OC.svelte';
  import AC from './lib/Pages/Team Pages/AC.svelte';
  import SoftwareTeam from './lib/Pages/Team Pages/SoftwareTeam.svelte';
  import CateringTeam from './lib/Pages/Team Pages/CateringTeam.svelte';
  import MediaTeam from './lib/Pages/Team Pages/MediaTeam.svelte';
  import ICJ from './lib/Pages/Team Pages/ICJ.svelte'
  import HRC from './lib/Pages/Team Pages/HRC.svelte';
  import ECOSOC from './lib/Pages/Team Pages/ECOSOC.svelte';
  import GA from './lib/Pages/Team Pages/GA.svelte'
  import JC from './lib/Pages/Team Pages/JC.svelte'
  import Construction from './lib/Pages/PageUnderConstruction.svelte';
  import SC from './lib/Pages/Team Pages/SC.svelte';
</script>



<Router>
  <Route path="/LogIn" component={LoginForm} />
  <Route path='/' component={Home} />
  <Route path='/about' component={AboutUs} />
  <Route path='/meet' component={MeetTeam} />
  <Route path='/meet/secretariat' component={Secretariat} />
  <Route path="/meet/oc" component={OC} />
  <Route path="/meet/ac" component={AC} />
  <Route path='/meet/oc/softwareteam' component={SoftwareTeam} />
  <Route path='/meet/oc/catering' component ={CateringTeam} />
  <Route path='/meet/oc/media' component ={MediaTeam} />
  <Route path='/meet/ac/ICJ' component = {ICJ} />
  <Route path='/meet/ac/HRC' component = {HRC}/>
  <Route path='/meet/ac/ECOSOC' component = {ECOSOC} />
  <Route path='/meet/ac/GA' component = {GA} />
  <Route path='/meet/ac/JC' component = {JC} />
  <Route path='/meet/ac/SC' component = {SC} />
</Router>


