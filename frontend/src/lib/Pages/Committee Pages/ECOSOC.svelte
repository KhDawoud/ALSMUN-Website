<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import TopicA from '../../../assets/Committees/ECOSOC/Topic 1.jpg';
    import TopicB from '../../../assets/Committees/ECOSOC/Topic 2.jpg';
    import InfoText from "../../Components/InfoText.svelte";
  
  </script>
  
  <NavBar />

  
  <h1 class="text-center font-bold underline text-6xl my-10"> Economic and Social Council </h1>
  <div class="grid grid-flow-row mx-auto space-y-8">
    <InfoText 
      image={TopicA}
      title="The Issue of the Petro Dollar"
      paragraphB=""
      paragraphA="In August 1971, President Nixon severed the direct convertibility of U.S. dollars into gold. With
      this decision, the international currency market, which had become increasingly reliant on the
      dollar since the enactment of the Bretton Woods Agreement, lost its formal connection to gold."
      link="https://drive.google.com/file/d/1Bv9Zk0z5lJTBCEyFLgcJwA2U8mJhmrMk/view?usp=sharing"    
      />

    <InfoText 
      image={TopicB}
      title="Topic 2: The Issue of Migration and Refugees"
      paragraphB="Economic differences between host communities and incoming
      refugees or immigrants can cause stress. Competition for jobs and goods can create social conflict and
      hinder the economic integration of displaced people.
      Host countries struggle to provide adequate resources and programs to the influx of refugees,
      creating problems in meeting basic needs such as housing, health and education
      Policy ineffectiveness: Inadequate or inadequate policy implementation on the integration of refugees
      and immigrants can exacerbate the issue. Inadequate support mechanisms and a lack of a clear path
      to citizenship can also hinder successful integration. Values and social practices between refugees and
      host communities can create barriers to effective communication and understanding, preventing
      social integration. Geopolitical tensions and instability in refugee areas of origin may contribute to
      the perpetuation of this issue. The continued influx of displaced persons places additional stress on
      host countries."
      paragraphA="The issue of integration and inclusion of refugees and migrants in host countries relates to the
      challenges and obstacles faced by individuals forced to flee their home countries due to conflict,
      persecution, or other crises.
      The issue stems primarily from undesirable migration for refugees. They are often forced to leave
      their homes as a result of war, violence, or other life-threatening situations, which can cause trauma
      and difficulty in adjusting. Many host countries have an immigrant background, a complex system
      that poses enormous challenges for refugees and migrants. Legal barriers, such as restrictive asylum
      procedures or lack of access to employment opportunities, can impede the integration process.
      Negative and negative perceptions of refugees and immigrants by the host community can contribute
      to their social exclusion. Discrimination based on national, ethnic, and religious beliefs can hinder the
      establishment of strong relationships. 
      "
      link="https://drive.google.com/file/d/1unzlp1B1RRio-2mPQjpREES_gC0CCBsc/view?usp=sharing"
      />
  </div>
  
  