<script lang="ts">
  import { Router, Route } from 'svelte-routing';
  import LoginForm from "./lib/Pages/LoginForm.svelte";
  import Home from './lib/Pages/Home.svelte';
  import AboutUs from './lib/Pages/AboutUs.svelte';
  import MeetTeam from './lib/Pages/Team Pages/MeetTeam.svelte';
  import Secretariat from './lib/Pages/Team Pages/Secretariat.svelte';
  import Oc from './lib/Pages/Team Pages/OC.svelte';
  import Ac from './lib/Pages/Team Pages/AC.svelte';
  import SoftwareTeam from './lib/Pages/Team Pages/SoftwareTeam.svelte';
</script>



<Router>
  <Route path="/LogIn" component={LoginForm} />
  <Route path='/' component={Home} />
  <Route path='/about' component={AboutUs} />
  <Route path='/meet' component={MeetTeam} />
  <Route path='/meet/secretariat' component={Secretariat} />
  <Route path="/meet/oc" component={Oc} />
  <Route path="/meet/ac" component={Ac} />
  <Route path='/meet/oc/softwareteam' component={SoftwareTeam} />
</Router>


