<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import JazminBlaj from "../../../assets/Secretariat/Jazmin Blaj.jpg"
    import MariamElRamly from "../../../assets/Secretariat/Mariam Elramly.jpg"
    import IbrahimZineldin from "../../../assets/Secretariat/Ibrahim Zineldin - DSG.jpg"
    import AdhamFayed from "../../../assets/Secretariat/Adham Fayed - USG.jpg"
    import GroupSection from "../../Components/GroupSection.svelte";
    import JBSignature from "../../../assets/Signatures/JB.png";
  </script>
  
  
  <NavBar />
  <header class="px-10">
      <h1 class=" text-4xl font-bold text-center mt-10"> Our Secretariat </h1>
      <hr class="mb-2 mt-4">  
  </header>
  <main class=" grid-flow-row grid-rows-4 m-5 space-y-4 p-5">
        <GroupSection link={null} noReadMe={true} header="Jazmin Blaj - Secretary General" text="Hey delegates! I'm Jazmin.

            It is a pleasure to act as your Secretary General this ALSMUN and will be an even greater pleasure to watch you all thrive and succeed at this conference. 
            I started off as a shy delegate 5 years ago, unsure of how my thoughts and opinions could or should be presented to others. MUN has helped me greatly to mould this skill and now I proudly hold my experiences at heart for the person I have grown to be. 
            
            I cannot wait to see you all!
            " image={JazminBlaj} signature={JBSignature}/>
        <GroupSection link={null} noReadMe={true} header="Ibrahim Zineldin - Deputy Secretary General" text={null} image={IbrahimZineldin} />
        <GroupSection link={null} noReadMe={true} header="Adham Fayed - Under Secretary General" text="Hi everyone! I’m Adham Fayed and I’m the Under Secretary General of ALSMUNII. I’m so excited to see you all at the conference. Being the USG of the conference has been such a fun experience and I look forward to being a part of ALSMUN in future years. I’ve been doing MUN since Grade 8 and I’ve been to 10 conferences. I am committed to ensuring a seamless and enriching experience for each delegate. I look forward to witnessing the diplomatic prowess of this assembly and contributing to the success of the El Alsson Model United Nations." image={AdhamFayed} />
        <GroupSection link={null} noReadMe={true} header="Mariam ElRamly - Assistant Secretary General" text="Hi! My name's Mariam and I'm this year's ALSMUNII Assistant Secretary General. I truly can't wait to share ALSMUNII with you all. This experience has honestly been one of a kind. It's been surreal working on this project. I've met so many amazing people along the way and formed so many connections and friendships that I'll never forget. MUN is an experience that I’ll forever be thankful for. It was extremely intimidating to me before I first started participating. But the serious looking students in delegates that wrote resolutions and attended conferences quickly became known to me as those who sing when they’re late and those who shout the house down during crisis. 

        I hope this conference will help you form memories as meaningful to you as they are to me." image={MariamElRamly} />
  </main>